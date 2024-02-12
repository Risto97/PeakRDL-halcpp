from typing import Union, Any
from abc import ABC, abstractmethod, abstractproperty

from systemrdl.node import Node


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

    def get_property(self, prop_name: str) -> Any:
        """Returns the SystemRDL node property."""
        return self._node.get_property(prop_name)

    def get_parent(self) -> Union['HalBase', None]:
        """Returns this node parent."""
        return self._parent

    @property
    def orig_type_name(self) -> str:
        if self._node.orig_type_name is not None:
            return self._node.orig_type_name
        else:
            return self._node.inst_name

    @property
    def type_name(self) -> str:
        """Returns the node type name property."""
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
