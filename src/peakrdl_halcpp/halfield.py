from typing import Dict

from systemrdl.node import FieldNode


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
