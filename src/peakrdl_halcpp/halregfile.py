from typing import TYPE_CHECKING, List

from systemrdl.node import RegNode, RegfileNode

from .halbase import HalBase
from .halreg import HalReg

if TYPE_CHECKING:
    from .haladdrmap import HalAddrmap


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

    def get_regs(self) -> List[HalReg]:
        return [HalReg(c, self) for c in self._node.children() if isinstance(c, RegNode)]

    def get_regfiles(self) -> List['HalRegfile']:
        regfiles_list = []
        for c in self._node.children():
            if isinstance(c, RegfileNode):
                regfiles_list.append(HalRegfile(c, self)) # type: ignore
        return regfiles_list

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
        return self.bus_offset + next(self._node.unrolled()).address_offset


class HalArrRegfile(HalRegfile):
    """HAL wrapper class for PeakRDL array of RegfileNode."""

    def __init__(self,
                 node: RegfileNode,
                 parent: 'HalAddrmap',
                 bus_offset: int = 0,
                 ):
        super().__init__(node, parent)

        self.bus_offset = bus_offset

        assert node.is_array, "Register File Node is not array"

        assert self._node.size == self._node.array_stride, f"Different stride than \
                                                            regwidth is not supported \
                                                            {self._node.size} \
                                                            {self._node.array_stride}"

    @property
    def addr_offset(self):
        return self.bus_offset + next(self._node.unrolled()).address_offset
