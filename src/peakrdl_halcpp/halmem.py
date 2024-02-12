from typing import List

from systemrdl.node import MemNode, AddressableNode

from .halbase import HalBase
from .haladdrmap import HalAddrmap


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
