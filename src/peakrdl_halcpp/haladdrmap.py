from typing import Union, List, Dict
from abc import ABC, abstractmethod, abstractproperty

from systemrdl.node import Node, AddrmapNode, RegNode, RootNode, MemNode, FieldNode, AddressableNode, RegfileNode


class HalBase(ABC):
    """Base abstract class for all the different HAL nodes (Addrmap, Reg, Mem, and Field).

    .. inheritance-diagram:: peakrdl_halcpp.haladdrmap
        :top-classes: peakrdl_halcpp.haladdrmap.HalBase
        :parts: 1

    Class methods:

    - :func:`get_docstring`
    - :func:`get_cls_tmpl_spec`
    - :func:`get_parent_haladdrmap`
    - :func:`get_template_line`
    """

    def __init__(self, node: Node, parent: Union['HalBase', None]):
        self._node = node
        self._parent = parent

    def get_docstring(self) -> str:
        """Converts the node description into a C++ multi-line comment.

        Returns
        -------
        str
            C++ multi-line comment string.
        """
        desc = "/*\n"
        if self._node.get_property('desc') is not None:
            for l in self._node.get_property('desc').splitlines():
                desc = desc + "* " + l + "\n"
            print(desc + "*/")
            return desc + "*/"
        return ""

    def get_parent_haladdrmap(self) -> 'HalAddrmap':
        if isinstance(self._parent, HalAddrmap):
            return self._parent
        assert self._parent is not None
        return self._parent.get_parent_haladdrmap()

    @property
    def orig_type_name(self) -> str:
        if self._node.orig_type_name is not None:
            return self._node.orig_type_name
        else:
            return self._node.inst_name

    @property
    def type_name(self) -> str:
        """Node type name property.

        Returns
        -------
        str
            String containing the node type name.
        """
        return self.orig_type_name

    @abstractproperty
    def addr_offset(self) -> int:
        """Node address offset property (relative address to parent node).
        It must be overloaded by the child class.

        Returns
        -------
        int
            Relative address offset to the parent node.
        """
        pass

    @abstractproperty
    def cpp_access_type(self) -> str:
        """Node access type (read and/or write) property. It must be
        overloaded by the child class.

        Returns
        -------
        str
            A string with the child class name followed by the access
            rights. For example, a field node with read only access
            would return 'FieldRO'.
        """
        pass

    @abstractmethod
    def get_template_line(self) -> str:
        """Returns the node C++ template line as a string. This method
        must be overloaded by the child class.

        This C++ string template (e.g., 'template<type MYVAR, ...>')

        Returns
        -------
        str
            C++ string template (e.g., 'template<type MYVAR, ...>') of the
            node type (e.g., reg, mem).
        """
        pass

    @abstractmethod
    def get_cls_tmpl_spec(self, just_tmpl: bool = False) -> str:
        """This method must be overloaded by the child class.

        Parameters
        ----------
        just_tmpl: (bool, optional)
            TBD. Defaults to False.

        Returns
        -------
        str
            C++ string template (e.g., TBD) of ?
        """
        pass


class HalField(HalBase):
    """HAL wrapper class for PeakRDL FieldNode.

    Class methods:

    - :func:`has_enum`
    - :func:`get_enum`
    - :func:`get_enum_name`
    - :func:`get_namespace_enums`
    - :func:`get_template_line`
    - :func:`get_cls_tmpl_spec`
    """

    def __init__(self, node: FieldNode, parent: 'HalReg'):
        super().__init__(node, parent)

    @property
    def width(self) -> int:
        return self._node.width

    def has_enum(self) -> bool:
        return self._node.get_property('encode', default=False) != False

    def get_enum(self):
        encode = self._node.get_property('encode')
        namespace_enums = self.get_namespace_enums()
        if encode is not None:
            name = encode.__name__
            if name in namespace_enums:
                if namespace_enums[name][-1] == self._node.owning_addrmap:  # TODO WHAT???
                    return False, None, None, None, None, None
            enum_strings = []
            enum_values = []
            enum_desc = []
            for k, v in encode.members.items():
                enum_strings.append(encode.members[k].name)
                enum_values.append(encode.members[k].value)
                enum_desc.append(encode.members[k].rdl_desc)

            const_width = max(enum_values).bit_length()

            namespace_enums[name] = [enum_strings, enum_values,
                                     enum_desc, const_width, self._node.owning_addrmap]
            return True, name, enum_strings, enum_values, enum_desc, const_width

        return False, None, None, None, None, None

    def get_enum_name(self):
        encode = self._node.get_property('encode')
        if encode is not None:
            return encode.__name__

    def get_namespace_enums(self) -> 'Dict':
        return self.get_parent_haladdrmap().enums

    @property
    def cpp_access_type(self) -> str:
        out = ""
        if self._node.is_sw_readable and self._node.is_sw_writable:
            return "FieldRW"
        elif self._node.is_sw_writable and not self._node.is_sw_readable:
            return "FieldWO"
        elif self._node.is_sw_readable:
            return "FieldRO"
        return out

    @property
    def addr_offset(self) -> int:
        assert False, "FieldNode has no offset"

    def get_template_line(self) -> str:
        assert False, "You should not create a class from a FieldNode"

    def get_cls_tmpl_spec(self, just_tmpl=False) -> str:
        assert False, "You should not extend FieldNode classes"


class HalReg(HalBase):
    """HAL wrapper class for PeakRDL RegNode."""

    def __init__(self,
                 node: RegNode,
                 parent: 'HalAddrmap|HalRegfile',
                 bus_offset: int = 0,
                 ):
        super().__init__(node, parent)
        self.bus_offset = bus_offset

        self.fields = self.get_fields()

    @property  # TODO move to base?
    def is_array(self) -> bool:
        return self._node.is_array

    @property
    def width(self) -> int:
        return max([c.node.high for c in self.fields]) + 1

    def get_fields(self) -> 'List[HalField]':
        return [HalField(c, self) for c in self._node.children() if isinstance(c, FieldNode)]

    @property
    def cpp_access_type(self):
        if self._node.has_sw_readable and self._node.has_sw_writable:
            return "RegRW"
        elif self._node.has_sw_writable and not self._node.has_sw_readable:
            return "RegWO"
        elif self._node.has_sw_readable:
            return "RegRO"
        assert False

    def get_template_line(self) -> str:
        return f"template<uint32_t BASE, uint32_t WIDTH, typename PARENT_TYPE>"

    def get_cls_tmpl_spec(self, just_tmpl=False) -> str:
        str = self.type_name.upper() if not just_tmpl else ""
        return str + "<BASE, WIDTH, PARENT_TYPE>"

    @property
    def addr_offset(self) -> int:
        return self.bus_offset + self._node.address_offset


class HalArrReg(HalReg):
    """HAL wrapper class for PeakRDL array of RegNode."""

    def __init__(self,
                 node: RegNode,
                 parent: 'HalAddrmap|HalRegfile',
                 bus_offset: int = 0,
                 ):
        super().__init__(node, parent)

        self.bus_offset = bus_offset

        assert node.is_array, "Register Node is not array"

        assert self._node.size == self._node.array_stride, f"Different stride than regwidth is not supported {self._node.size} {self._node.array_stride}"

    @property
    def addr_offset(self):
        # type: ignore
        return self.bus_offset + next(self._node.unrolled()).address_offset


class HalMem(HalBase):
    """HAL wrapper class for PeakRDL MemNode."""

    def __init__(self,
                 node: MemNode,
                 parent: 'HalAddrmap',
                 bus_offset: int = 0,
                 ):
        super().__init__(node, parent)

        self.bus_offset = bus_offset

        for c in self._parent.node.children():
            if isinstance(c, AddressableNode):
                assert c == self._node, f"Addrmaps with anything else than one memory node is currently not allowed, it could be easily added"

    @property
    def size(self) -> int:
        return self._node.size

    @property
    def width(self) -> int:  # TODO probably not good
        return self.size

    def get_template_line(self) -> str:
        return f"template<uint32_t BASE, uint32_t SIZE, typename PARENT_TYPE>"

    @property
    def cpp_access_type(self) -> str:
        assert False, "cpp_access_type should not be called on HalMem class"

    def get_cls_tmpl_spec(self, just_tmpl=False) -> str:
        str = self.type_name.upper() if not just_tmpl else ""
        return str + "<BASE, SIZE, PARENT_TYPE>"

    @property
    def type_name(self) -> str:
        return self._parent.orig_type_name

    @property
    def addr_offset(self) -> int:
        return self.bus_offset + self._node.address_offset


class HalRegfile(HalBase):
    """HAL wrapper class for PeakRDL RegfileNode."""

    def __init__(self,
                 node: RegfileNode,
                 parent: 'HalAddrmap',
                 bus_offset: int = 0
                 ):
        super().__init__(node, parent)
        self.bus_offset = bus_offset

        self.regs = self.get_regs()
        self.regfiles = self.get_regfiles()

    @property  # TODO move to base?
    def is_array(self) -> bool:
        return self._node.is_array

    # @property
    # def width(self) -> int:
    #     return max([c.node.high for c in self.]) + 1

    def get_regs(self) -> 'List[HalReg]':
        return [HalReg(c, self) for c in self._node.children() if isinstance(c, RegNode)]

    def get_regfiles(self) -> 'List[HalRegfile]':
        return [HalRegfile(c, self) for c in self._node.children() if isinstance(c, RegfileNode)]

    @property
    def cpp_access_type(self):
        return "RegfileNode"

    def get_template_line(self) -> str:
        return f"template<uint32_t BASE, typename PARENT_TYPE>"

    def get_cls_tmpl_spec(self, just_tmpl=False) -> str:
        str = self.type_name.upper() if not just_tmpl else ""
        return str + "<BASE, PARENT_TYPE>"

    @property
    def addr_offset(self) -> int:
        # type: ignore
        return self.bus_offset + next(self._node.unrolled()).address_offset


class HalArrRegfile(HalRegfile):
    """HAL wrapper class for PeakRDL array of RegfileNode."""

    def __init__(self,
                 node: RegfileNode,
                 parent: 'HalAddrmap|HalRegfile',
                 bus_offset: int = 0,
                 ):
        super().__init__(node, parent)

        self.bus_offset = bus_offset

        assert node.is_array, "Register File Node is not array"

        assert self._node.size == self._node.array_stride, f"Different stride than regwidth is not supported {self._node.size} {self._node.array_stride}"

    @property
    def addr_offset(self):
        # type: ignore
        return self.bus_offset + next(self._node.unrolled()).address_offset


class HalAddrmap(HalBase):
    """HAL wrapper class for PeakRDL AddrmapNode.

    Class methods:


    """

    def __init__(self,
                 node: AddrmapNode,
                 parent: 'HalAddrmap|None' = None,
                 bus_offset: int = 0
                 ):
        super().__init__(node, parent)

        # What is this bus offset?
        self.bus_offset = bus_offset

        # Check that top level HAL has no parent but RootNode
        assert (self._parent == None) == isinstance(self._node.parent, RootNode)

        # Traverse all the node hierarchy and extract of the different nodes:
        # RegNode -> HalReg or HalArrReg
        self.regs = self.get_regs()
        # Regfile -> HalRegfile or HalArrRegfile
        self.regfiles = self.get_regfiles()
        # MemNode -> HalMem
        self.mems = self.get_mems()
        # AddrMapNode -> HalAddrMap
        self.addrmaps = self.get_addrmaps()

        self.enums = {}

    @property
    def is_top_node(self) -> bool:
        """Check if this is the top node.

        Returns
        -------
            bool
                Returns True if the node is the top one (i.e., no parent).
        """
        return self._parent == None

    def get_regs(self) -> 'List[HalReg]':
        """Traverses the node hierarchy and extracts the RegNodes and the
        array of RegNodes.

        Returns
        -------
        List[HalReg]
            List of RegNode objects each encapsulated in a HalReg (or HalArrReg) object.
        """
        regs = []
        for c in self._node.children():
            if isinstance(c, RegNode):
                reg = HalArrReg(c, self) if c.is_array else HalReg(c, self)
                regs.append(reg)
        return regs

    def get_mems(self) -> 'List[HalMem]':
        """Traverses the node hierarchy and extracts the MemNodes.

        Returns
        -------
        List[HalMem]
            List of MemNode objects each encapsulated in a HalMem object.
        """
        return [HalMem(c, self) for c in self._node.children() if isinstance(c, MemNode)]

    def get_addrmaps(self) -> 'List[HalAddrmap]':
        """Traverses the node hierarchy and extracts the AddrmapNode.

        Returns
        -------
        List[HalMem]
            List of AddrmapNode objects each encapsulated in a HalAddrmap object.
        """
        return [HalAddrmap(c, self) for c in self._node.children() if isinstance(c, AddrmapNode)]

    def get_regfiles(self) -> 'List[HalRegfile]':
        """Traverses the node hierarchy and extracts the RegfileNodes and the
        array of RegfileNodes.

        Returns
        -------
        List[HalReg]
            List of RegfileNode objects each encapsulated in a HalRegfile (or HalArrRegfile) object.
        """
        regfiles = []
        for c in self._node.children():
            if isinstance(c, RegfileNode):
                regfile = HalArrRegfile(
                    c, self) if c.is_array else HalRegfile(c, self)
                regfiles.append(regfile)
        return regfiles

    def remove_buses(self):
        """Removes buses (i.e., addrmaps containing only addrmaps).

        The address offset of the current AddrMapNode is added to each of
        its child AddrMapNodes and the parent node of the current AddrMapNode is
        passed to its child AddrMapNodes.
        """
        remove_list = []
        for c in self.addrmaps:
            c.remove_buses()
            if c.is_bus():
                # Traverse the child AddrMapNodes and add to them the address
                # offset of the current AddrMapNode and update their parent
                for subc in c.addrmaps:
                    subc.bus_offset += c.addr_offset
                    subc._parent = self
                remove_list.append(c)
                # Extend the addrmaps list with the removed node one
                self.addrmaps.extend(c.addrmaps)

        [self.addrmaps.remove(c) for c in remove_list]

    def is_bus(self) -> bool:
        """Checks if the addrmap is a bus.

        Returns
        -------
        bool
            Returns True if the addrmap is a bus (i.e., addrmaps containing only addrmaps).
        """
        if len(self.regs) == 0 and len(self.mems) == 0 and len(self.regfiles) == 0:
            return True
        return False

    def get_regfiles_regs(self) -> 'List[HalReg]':
        """Extracts the registers from the regfiles.

        Returns
        -------
            List[HalReg]
                List of registers (HalReg) contained in the node regfiles.
        """        
        regs = []
        for regfile in self.regfiles:
            regs.extend(regfile.regs)
        return regs

    def get_template_line(self) -> str:
        """Returns the HAL template for AddrmapNode.

        Returns
        -------
            str
                C++ template structure for AddrmapNode.
        """
        if self.is_top_node:
            # Parent is set to void by default for the top node
            return "template <uint32_t BASE, typename PARENT_TYPE=void>"
        return "template <uint32_t BASE, typename PARENT_TYPE>"
    
    def get_cls_tmpl_spec(self, just_tmpl=False) -> str:
        """Returns the HAL template parameters used for forwarding reference.

        The structure must matched the template returned by :func:`get_template_line`.

        Returns
        -------
            str
                C++ template parameters.
        """
        str = self.type_name.upper() if not just_tmpl else ""

        if self.is_top_node:
            return str + "<BASE, PARENT_TYPE>"
        return str + "<BASE, PARENT_TYPE>"

    @property
    def type_name(self) -> str:
        return self.orig_type_name + "_hal"

    @property
    def cpp_access_type(self) -> str:
        assert False, "cpp_access_type not defined (is it needed?)"

    def get_addrmaps_recursive(self):
        addrmaps = self.addrmaps.copy()
        for c in self.addrmaps:
            addrmaps.extend(c.get_addrmaps_recursive())
        if self.is_top_node:
            addrmaps.insert(0, self)
        return addrmaps

    @property
    def addr_offset(self) -> int:
        return self.bus_offset + self._node.address_offset
