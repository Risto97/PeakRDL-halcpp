from typing import List
import getpass
import datetime

from .haladdrmap import *

class HalUtils():
    """
    This is the top level C++ HAL exporter class. This class is called
    by the do_export() call of the PeakRDL plugin Exporter class.

    Methods
    -------
    get_include_file(halnode : HalAddrmap) -> str:
        TBD
    has_extern(halnode : HalAddrmap) -> bool:
        TBD
    get_extern(halnode : HalAddrmap) -> str:
        TBD
    get_unique_type_nodes(lst : 'List[HalBase]'):
        TBD
    generate_file_header():
        TBD
    build_hierarchy(node : AddrmapNode, keep_buses : bool = False,
                    remove_root: bool = True)
                    -> HalAddrmap : top = HalAddrmap(node)
        TBD
    """
    def __init__(self, extern : List[str]) -> None:
        """
        Initialize the extern variable with a list of external
        functionalities to include to the HAL (i.e., 'higher level' functions).
        """
        self.extern = extern

    def get_include_file(self, halnode : HalAddrmap) -> str:
        """

        """
        has_extern = self.has_extern(halnode)
        return halnode.orig_type_name + "_ext.h" if has_extern else halnode.type_name + ".h"

    def has_extern(self, halnode : HalAddrmap) -> bool:
        """
        Returns True if the object contains external files (i.e., extern).
        """
        if self.extern is not None:
            if halnode.orig_type_name in self.extern:
                return True
        return False

    def get_extern(self, halnode : HalAddrmap) -> str:
        if self.has_extern(halnode):
            return halnode.orig_type_name
        return halnode.type_name

    def get_unique_type_nodes(self, lst : 'List[HalBase]'):
        return list({node.type_name: node for node in lst}.values())

    def generate_file_header(self):
        username = getpass.getuser()
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        comment = f"// Generated with PeakRD-halcpp : https://github.com/Risto97/PeakRDL-halcpp\n"
        comment += f"// By user: {username} at: {current_datetime}\n"
        return comment

    def build_hierarchy(self,
                        node : AddrmapNode,
                        keep_buses   : bool=False,
                        remove_root  : bool=True,
                        ) -> HalAddrmap:
        """
        TBD

        Parameters
        -------
        node : AddrmapNode
            TBD
        keep_buses : bool=False
            TBD
        remove_root : bool=True
            TBD

        Returns
        -------
        HalAddrmap
            TBD
        """

        # Initialize the HAL top address map (i.e., no parent)
        top = HalAddrmap(node)

        if keep_buses is False:
            top.remove_buses()

        return top
