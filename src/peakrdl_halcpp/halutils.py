from systemrdl import RDLWalker, RDLListener
from systemrdl.node import Node, MemNode, RootNode, AddressableNode, RegNode, FieldNode
from typing import List, Union
import jinja2
import os
import copy


class HalListener(RDLListener):
    def __init__(self):
        self.addrmaps = []

    def enter_Addrmap(self, node):
        self.addrmaps.append(node)      

class HalUtils():
    
    def __init__(self, 
            ext_classes=[],
            remove_buses : bool=False,
            ):
        if ext_classes is None:
            ext_classes = []
        self.ext_classes = ext_classes 

        self.remove_buses = remove_buses

    def isRootNode(self, node : Node):
        return isinstance(node, RootNode)

    def isMemNode(self, node : Node):
        return isinstance(node, MemNode)

    def isRegNode(self, node : Node):
        return isinstance(node, RegNode)

    def isAddressableNode(self, node : Node):
        return isinstance(node, AddressableNode)

    def getIncludeLine(self, node : Node):
        out = '#include"'
        type_name = self.getTypeName(node)
        has_extern = self.hasExtern(type_name)
        if has_extern:
            return out + type_name + '_ext.h"'
        else:
            return out + type_name + '_hal.h"'

    def getAddressableNodes(self, node : Node):
        nodes = []
        for c in node.children():
            if isinstance(c, AddressableNode):
                nodes.append(c)
        return nodes

    def hasExtern(self, name : str) -> bool:
        for ext in self.ext_classes:
            if ext == name:
                return True
        return False

    def findExtern(self, name : str) -> str:
        for ext in self.ext_classes:
            if ext == name:
                return ext + "_ext"
        return name

    def getMemberNodes(self, node : Node):
        nodes = []
        addr_nodes = self.getAddressableNodes(node)

        if self.remove_buses:
            for c in addr_nodes:
                if self.isBus(c):
                    for bus_c in self.getAddressableNodes(c):
                        bus_c.inst.addr_offset = bus_c.inst.addr_offset + c.inst.addr_offset  # TODO, possibly unsafe, find better way to do it
                        nodes.append(bus_c)
                    addr_nodes.remove(c)

        nodes = nodes + addr_nodes 
        return nodes
            

    def getDocstring(self, node: Node):
        desc = "/*\n"
        if node.get_property('desc') is not None:
            for l in node.get_property('desc').splitlines():
                desc = desc + "* " + l + "\n"
            return desc + "*/"
        return  ""

    def getRegNodes(self, node : Node):
        nodes = []
        for c in node.children():
            if isinstance(c, RegNode):
                nodes.append(c)
        return nodes

    def isUnique(self, node: Node, unique_list : List[Node]):
        for n in unique_list:
            if self.getTypeName(n) == self.getTypeName(node):
                return False
        return True


    def getMemNodes(self, node: Node):
        nodes = []
        for c in node.children():
            if isinstance(c, MemNode):
                nodes.append(c)

        return nodes


    def filterUniqueTypes(self, node : Union[Node, List[Node]]):
        unique_list = []
        child_list = []
        if isinstance(node, Node):
            child_list = node.children()

        if isinstance(node, list):
            child_list = node

        for c in child_list:
            if self.isUnique(c, unique_list):
                unique_list.append(c)

        return unique_list

    def getTypeName(self, node : Node):
        if node.orig_type_name is not None:
            return node.orig_type_name
        else:
            return node.inst_name

    def getTemplateLine(self, node : Node):
        if self.isRootNode(node.parent):
            return "template <uint32_t BASE>"
        elif self.isMemNode(node):
            return f"template<uint32_t BASE, uint32_t SIZE, typename PARENT_TYPE>"
        else:
            return "template <uint32_t BASE, typename PARENT_TYPE>"

    def getClsTmplSpec(self, node: Node, just_tmpl=False):
        str = ""
        if not just_tmpl:
            str = str + self.getTypeName(node).upper()

        if self.isRootNode(node.parent):
            return str + "<BASE>"
        elif self.isMemNode(node):
            return str + "<BASE, SIZE, PARENT_TYPE>"
        else:
            return str + "<BASE, PARENT_TYPE>"

    def isBus(self, node : Node):
        return self.hasOnlyAddrmaps(node)

    def hasOnlyAddrmaps(self, node : Node):
        for c in node.children():
            if isinstance(c, (RegNode, MemNode, FieldNode)):
                return False
        return True

    def copyBusesChildren(self, node : Node, bus : Node):
        for c in bus.children():
            node.inst.children.append(c)

    def getAddrmapNodes(self, node : Node, remove_root=True):
        walker = RDLWalker(unroll=True)
        listener = HalListener()
        walker.walk(node, listener)
        addrmaps = listener.addrmaps

        if remove_root:
            addrmaps.remove(node)

        if self.remove_buses is True:
            for n in addrmaps:
                if self.isBus(n):
                    addrmaps.remove(n)

        if addrmaps is None:
            return []

        return addrmaps

    def process_template(self, context : dict, template : str) -> str:

        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader('%s/templates/' % os.path.dirname(__file__)),
            trim_blocks=True,
            lstrip_blocks=True)

        env.filters.update({
            'isRootNode' : self.isRootNode,
            'isMemNode' : self.isMemNode,
            'isRegNode' : self.isRegNode,
            'isAddressableNode' : self.isAddressableNode,
            'getAddressableNodes' : self.getAddressableNodes,
            'getRegNodes' : self.getRegNodes,
            'getAddrmapNodes' : self.getAddrmapNodes,
            'getMemNodes' : self.getMemNodes,
            # 'getFieldNodes' : self.getFieldNodes,
            'getTypeName' : self.getTypeName,
            'getIncludeLine' : self.getIncludeLine,
            'findExtern' : self.findExtern,
            'getMemberNodes' : self.getMemberNodes,
            'filterUniqueTypes' : self.filterUniqueTypes,
            'getClsTmplSpec' : self.getClsTmplSpec,
            'getTemplateLine' : self.getTemplateLine,
            'getDocstring' : self.getDocstring,
            })

        res = env.get_template(template).render(context)
        return res

