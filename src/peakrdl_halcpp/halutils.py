from typing import List, Type, Dict, Union
import getpass
import datetime

from systemrdl.node import AddrmapNode

from .halbase import HalBase
from .haladdrmap import HalAddrmap


class HalUtils():
    """
    HAL utility class.

    Class methods:

    - :func:`get_include_file`
    - :func:`has_extern`
    - :func:`get_extern`
    - :func:`get_unique_type_nodes`
    - :func:`generate_file_header`
    - :func:`build_hierarchy`
    """

    def __init__(self, ext_modules: List[str]) -> None:
        """Initializes the ext_modules variable with a list of external
        modules implementing extended functionalities (e.g., a read_gpio_port()
        function) to be included to the HAL.

        Parameters
        ----------
        ext_modules: List[str]
            List of modules (i.e., SystemRDL addrmap objects) with extended functionalities.
        """
        self.ext_modules = ext_modules

    def get_include_file(self, halnode: HalAddrmap) -> str:
        """Returns the HAL node base header file or the extended header file
        if the later exists.
        """
        has_extern = self.has_extern(halnode)
        return halnode.orig_type_name + "_ext.h" if has_extern else halnode.type_name + ".h"

    def has_extern(self, halnode: HalAddrmap) -> bool:
        """Returns True if the HAL node is listed as having extended functionalities."""
        if self.ext_modules is not None:
            if halnode.orig_type_name in self.ext_modules:
                return True
        return False

    def get_extern(self, halnode: HalAddrmap) -> str:
        """Return the ??? name of the HAL node.

        Parameters
        ----------
            halnode: HalAddrmap
                HAL node corresponding to a SystemRDL addrmap object.

        Returns
        -------
            str: ???
        """
        if self.has_extern(halnode):
            return halnode.orig_type_name
        return halnode.type_name

    def get_unique_type_nodes(self, halnode_lst: List[HalBase]):
        """Returns a list of names (str)

        Parameters
        ----------
        halnode_lst: List[HalBase]
            List of objects based on the HalBase abstract class.

        Returns
        -------
        _type_
            _description_
        """
        return list({halnode.type_name: halnode for halnode in halnode_lst}.values())

    def generate_file_header(self) -> str:
        """Returns file header for generated files."""
        username = getpass.getuser()
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        comment = f"// Generated with PeakRD-halcpp : https://github.com/Risto97/PeakRDL-halcpp\n"
        comment += f"// By user: {username} at: {current_datetime}\n"
        return comment

    def get_owning_addrmap(self, node: HalBase) -> Union[HalBase, HalAddrmap]:
        """Returns the HalAddrmap enclosing this node."""
        parent_node = node.get_parent()
        if isinstance(parent_node, HalAddrmap):
            return parent_node
        elif parent_node is not None:
            return self.get_owning_addrmap(parent_node)
        else:
            raise ValueError(f'No HalAddrmap parent found in the hierarchy.')

    def get_node_enum(self, node: HalBase):
        encode = node.get_property('encode')
        if encode is not None:
            haladdrmap_node = self.get_owning_addrmap(node)
            if not isinstance(haladdrmap_node, HalAddrmap):
                raise ValueError(f'Returned node is not an HalAddrmap object.')

            # Each addrmap is enclosed in a specific namespace
            # Get this namespace enums and add the new ones
            namespace_enums = haladdrmap_node.enums

            # Check the enum encoding is not already in the namespace
            name = encode.__name__
            if name in namespace_enums:
                # Is this check really needed?
                # It should always be true, because if its not then the above check should not be true
                # TODO WHAT???
                if namespace_enums[name][-1] == node.get_property('owning_addrmap'):
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
                                     enum_desc, const_width, node.get_property('owning_addrmap')]
            return True, name, enum_strings, enum_values, enum_desc, const_width

        return False, None, None, None, None, None

    def build_hierarchy(self, node: AddrmapNode, keep_buses: bool = False) -> HalAddrmap:
        """Build the hierarchy using the HAL wrapper classes around PeakRDL
        nodes (e.g., AddrmapNodes, RegNodes)

        Parameters
        ----------
        node: AddrmapNode
            Top level AddrmapNode of the SystemRDL description
        keep_buses: (bool, optional)
            Keep AddrMapNodes containing only AddrMapNodes. Defaults to False.

        Returns
        -------
        HalAddrmap
            HalAddrmap top class containing the HAL wrapper class hierarchy.
        """

        # Initialize the HAL top address map (i.e., no parent)
        top = HalAddrmap(node)
        # By default the buses (i.e., addrmaps containing only addrmaps) are removed
        if keep_buses is True:
            return top
        else:
            # Could this be a nice one liner?
            top.remove_buses()
            return top
