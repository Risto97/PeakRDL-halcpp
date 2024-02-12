from typing import TYPE_CHECKING, List

from systemrdl.node import RegNode, FieldNode

from .halbase import HalBase
from .halfield import HalField

if TYPE_CHECKING:
    from .halregfile import HalRegfile
    from .haladdrmap import HalAddrmap


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
        return max([c._node.high for c in self.fields]) + 1

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
        return self.bus_offset + next(self._node.unrolled()).address_offset
