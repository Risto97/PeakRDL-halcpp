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

        self.fields = self._get_fields()

    def _get_fields(self) -> 'List[HalField]':
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
        """Returns the HAL C++ template for RegNode class.

        Returns
        -------
            str
                C++ template structure for RegNode class.
        """
        return f"template <uint32_t BASE, uint32_t WIDTH, typename PARENT_TYPE>"

    def get_cls_tmpl_params(self) -> str:
        """Returns the HAL template parameters for class object reference.

        The structure must matched the template returned by :func:`get_template_line`.

        Returns
        -------
            str
                C++ template parameters.
        """
        return "<BASE, WIDTH, PARENT_TYPE>"

    @property
    def addr_offset(self) -> int:
        """Returns the node address offset relative to its parent."""
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

        assert self._node.size == self._node.array_stride, (f"Different stride than \
                                                            regwidth is not supported \
                                                            {self._node.size} {self._node.array_stride}")

    @property
    def addr_offset(self):
        return self.bus_offset + next(self._node.unrolled()).address_offset
