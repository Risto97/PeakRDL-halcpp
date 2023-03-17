from systemrdl import RDLWalker, RDLListener
from systemrdl.node import Node, MemNode, RootNode, AddressableNode, RegNode
from typing import List, Union
import jinja2
import os


class HalListener(RDLListener):
    def __init__(self):
        self.addrmaps = []

    def enter_Addrmap(self, node):
        self.addrmaps.append(node)      

def isRootNode(node : Node):
    return isinstance(node, RootNode)

def isMemNode(node : Node):
    return isinstance(node, MemNode)

def isRegNode(node : Node):
    return isinstance(node, RegNode)

def isAddressableNode(node : Node):
    return isinstance(node, AddressableNode)

def getAddressableNodes(node : Node):
    nodes = []
    for c in node.children():
        if isinstance(c, AddressableNode):
            nodes.append(c)
    return nodes

def getDocstring(node: Node):
    desc = "/*\n"
    if node.get_property('desc') is not None:
        for l in node.get_property('desc').splitlines():
            desc = desc + "* " + l + "\n"
        return desc + "*/"
    return  ""

def getRegNodes(node : Node):
    nodes = []
    for c in node.children():
        if isinstance(c, RegNode):
            nodes.append(c)
    return nodes

def isUnique(node: Node, unique_list : List[Node]):
    for n in unique_list:
        if getTypeName(n) == getTypeName(node):
            return False
    return True


def getMemNodes(node: Node):
    nodes = []
    for c in node.children():
        if isinstance(c, MemNode):
            nodes.append(c)

    return nodes


def filterUniqueTypes(node : Union[Node, List[Node]]):
    unique_list = []
    child_list = []
    if isinstance(node, Node):
        child_list = node.children()

    if isinstance(node, list):
        child_list = node

    for c in child_list:
        if isUnique(c, unique_list):
            unique_list.append(c)

    return unique_list

def getTypeName(node : Node):
    if node.orig_type_name is not None:
        return node.orig_type_name
    else:
        return node.inst_name

def getTemplateLine(node : Node):
    if isRootNode(node.parent):
        return "template <uint32_t BASE>"
    elif isMemNode(node):
        return f"template<uint32_t BASE, uint32_t SIZE, typename PARENT_TYPE>"
    else:
        return "template <uint32_t BASE, typename PARENT_TYPE>"

def getClsTmplSpec(node: Node, just_tmpl=False):
    str = ""
    if not just_tmpl:
        str = str + getTypeName(node).upper()

    if isRootNode(node.parent):
        return str + "<BASE>"
    elif isMemNode(node):
        return str + "<BASE, SIZE, PARENT_TYPE>"
    else:
        return str + "<BASE, PARENT_TYPE>"

def getAddrmapNodes(node : Node, remove_root=True):
    walker = RDLWalker(unroll=True)
    listener = HalListener()
    walker.walk(node, listener)
    addrmaps = listener.addrmaps

    if remove_root:
        addrmaps.remove(node)
    if addrmaps is None:
        return []

    return addrmaps

def process_template(context : dict, template : str) -> str:

    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader('%s/templates/' % os.path.dirname(__file__)),
        trim_blocks=True,
        lstrip_blocks=True)

    env.filters.update({
        'isRootNode' : isRootNode,
        'isMemNode' : isMemNode,
        'isRegNode' : isRegNode,
        'isAddressableNode' : isAddressableNode,
        'getAddressableNodes' : getAddressableNodes,
        'getRegNodes' : getRegNodes,
        'getAddrmapNodes' : getAddrmapNodes,
        'getMemNodes' : getMemNodes,
        # 'getFieldNodes' : getFieldNodes,
        'getTypeName' : getTypeName,
        'filterUniqueTypes' : filterUniqueTypes,
        'getClsTmplSpec' : getClsTmplSpec,
        'getTemplateLine' : getTemplateLine,
        'getDocstring' : getDocstring,
        })

    res = env.get_template(template).render(context)
    return res

