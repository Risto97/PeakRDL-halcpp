from typing import TYPE_CHECKING

from systemrdl.node import FieldNode

from .halbase import HalBase

if TYPE_CHECKING:
    from .halreg import HalReg


class HalField(HalBase):
    """HAL wrapper class for PeakRDL FieldNode.

    Class methods:

    - :func:`get_template_line`
    - :func:`get_cls_tmpl_spec`
    """

    def __init__(self, node: FieldNode, parent: 'HalReg'):
        super().__init__(node, parent)

    @property
    def width(self) -> int:
        return self._node.width

    @property
    def cpp_access_type(self) -> str:
        out = ""
        if self._node.is_sw_readable and self._node.is_sw_writable:
            return "FieldRW"
        elif self._node.is_sw_writable and not self._node.is_sw_readable:
            return "FieldWO"
        elif self._node.is_sw_readable:
            return "FieldRO"
        else:
            raise ValueError (f'Node field access rights are not found \
                              {self._node.orig_type_name}')

    @property
    def addr_offset(self) -> int:
        assert False, "FieldNode has no offset"

    def get_template_line(self) -> str:
        assert False, "You should not create a class from a FieldNode"

    def get_cls_tmpl_params(self, just_tmpl=False) -> str:
        assert False, "You should not extend FieldNode classes"
