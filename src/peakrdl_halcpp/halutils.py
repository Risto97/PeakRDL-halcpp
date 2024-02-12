from typing import List
import getpass
import datetime

from .haladdrmap import *


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
        """Returns True if the HAL node is listed as having extended functionalities.
        """
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

    def get_unique_type_nodes(self, lst: List[HalBase]):
        return list({node.type_name: node for node in lst}.values())

    def generate_file_header(self):
        username = getpass.getuser()
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        comment = f"// Generated with PeakRD-halcpp : https://github.com/Risto97/PeakRDL-halcpp\n"
        comment += f"// By user: {username} at: {current_datetime}\n"
        return comment

    def build_hierarchy(self, node: AddrmapNode, keep_buses: bool = False) -> HalAddrmap:
        """Build the hierachy using the HAL wrapper classes around PeakRDL
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
