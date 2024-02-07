import os
from typing import TYPE_CHECKING
import shutil

import jinja2 as jj
from systemrdl.node import Node, RootNode, AddrmapNode

from .haladdrmap import *
from .halutils import HalUtils

# Import the different types if checking is activated
if TYPE_CHECKING:
    from typing import Union, Any, List, str, bool, Dict


class HalExporter():
    """This method will be used to add two numbers

        :param int num1: The first number
        :param int num2: The second number

        :returns: The sum of two numbers

        :rtype: int
    """


    def __init__(self, **kwargs: 'Any'):
        # Check for stray kwargs
        if kwargs:
            raise TypeError("got an unexpected keyword argument '%s'" %
                            list(kwargs.keys())[0])

        # Include files generated output directory
        self.cpp_dir = "include"
        # HAL C++ base headers list (copied into cpp_dir)
        self.base_headers = [
            "halcpp_base.h",
            "halcpp_utils.h",
            "field_node.h",
            "reg_node.h",
            "regfile_node.h",
            "array_nodes.h",
            "addrmap_node.h",
            "arch_io.h",
        ]

    def list_files(self, top: HalAddrmap, outdir: str):
        """
        Prints the generated files to stdout (without generating the files).

        Parameters
        ----------
        top: HalAddrmap
            Top level HalAddrmap object.
        outdir: str
            Output directory to which the generated files would be put.
        """
        gen_files = [os.path.join(outdir, addrmap.type_name + ".h")
                     for addrmap in top.get_addrmaps_recursive()]
        # Create base header files path
        base_files = [os.path.join(self.cpp_dir, x) for x in self.base_headers]
        # Add the base header files to the list of files
        out_files = [os.path.join(outdir, x) for x in base_files] + gen_files
        print(*out_files, sep="\n")

    def copy_base_headers(self, outdir: str):
        """
        Copies the HAL base headers to the generated HAL files location given
        by outdir.

        Parameters
        ----------
        outdir: str
            Output directory to which the generated files would be put.
        """
        abspaths = [os.path.join(os.path.dirname(
            __file__), self.cpp_dir, x) for x in self.base_headers]
        outdir = os.path.join(outdir, "include")
        if not os.path.exists(outdir):
            os.makedirs(outdir)
        [shutil.copy(x, outdir) for x in abspaths]

    def export(self, node: 'Union[AddrmapNode, RootNode]', outdir: str, list_files: bool = False, ext: List = [], keep_buses: bool = False) -> None:
        """
        Plugin exporter main function.

        Parameters
        ----------
        nodes: Union[Node, List[Node]]
        outdir: str
        list_files: bool=False
        ext: list=[]
        keep_buses: bool=False
        """

        # print("+++++++++++DEBUG+++++++++++++++")
        # print(f'Node type: {type(node)}')
        # print(f'Node: {node}')
        # print(f'Node address offset: {node.inst.addr_offset}')
        # print(f'Node original type name: {node.orig_type_name}')
        # desc = "/*\n"
        # if node.get_property('desc') is not None:
        #     for l in node.get_property('desc').splitlines():
        #         desc = desc + "* " + l + "\n"
        # print(f'Node description:\n{desc}*/')
        # print("+++++++++++++++++++++++++++++++")

        # If it is the root node, skip to top addrmap
        if isinstance(node, RootNode):
            node = node.top
        # Check the node is an AddrmapNode object
        if not isinstance(node, AddrmapNode):
            raise TypeError(
                "'node' argument expects type AddrmapNode. Got '%s'" % type(node).__name__)

        halutils = HalUtils(ext)

        top = halutils.build_hierarchy(
            node=node,
            remove_root=False,  # TODO fix
            keep_buses=keep_buses,
        )

        if list_files:
            self.list_files(top, outdir)
        else:
            # Create the output directory for the generated files
            try:
                os.makedirs(outdir)
            except FileExistsError:
                pass

            for halnode in top.get_addrmaps_recursive():
                context = {
                    'halnode': halnode,
                    'halutils': halutils,
                }
                text = self.process_template(context)
                out_file = os.path.join(outdir, halnode.type_name + ".h")
                with open(out_file, 'w') as f:
                    f.write(text)

            self.copy_base_headers(outdir)

    def process_template(self, context: Dict) -> str:

        env = jj.Environment(
            loader=jj.FileSystemLoader(
                '%s/templates/' % os.path.dirname(__file__)),
            trim_blocks=True,
            lstrip_blocks=True)

        # Benoit: what does it do?
        env.filters.update({
            'zip': zip,
        })

        res = env.get_template("addrmap.j2").render(context)
        return res
