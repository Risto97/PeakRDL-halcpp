from systemrdl.node import  Node, RootNode, AddrmapNode
from typing import List, Union
import os
import shutil

from .halutils import *

class HalExporter():
    def __init__(self):
        self.cpp_dir = "templates"

        self.base_headers = [
                "halcpp_base.h",
                "halcpp_utils.h",
                "field_node.h",
                "reg_node.h",
                "addrmap_node.h",
                "arch_io.h",
                ]

    def list_files(self, addrmaps : List[AddrmapNode], outdir : str, utils : HalUtils):
        out_files = [os.path.join(outdir, utils.getTypeName(node) + ".h") for node in addrmaps]
        out_files = [os.path.join(outdir, x) for x in self.base_headers] + out_files
        print(*out_files) # Print files to stdout

    def copy_base_headers(self, outdir):
        abspaths = [os.path.join(os.path.dirname(__file__), self.cpp_dir, x) for x in self.base_headers]
        [shutil.copy(x, outdir) for x in abspaths]

    def export(self,
            nodes: 'Union[Node, List[Node]]',
            outdir: str, 
            list_files: bool=False,
            ext : list=[],
            **kwargs: 'Dict[str, Any]') -> None:


        # if not a list
        if not isinstance(nodes, list):
            nodes = [nodes]

        # If it is the root node, skip to top addrmap
        for i, node in enumerate(nodes):
            if isinstance(node, RootNode):
                nodes[i] = node.top

        if kwargs:
            raise TypeError("got an unexpected keyword argument '%s'" % list(kwargs.keys())[0])

        try:
            os.makedirs(outdir)
        except FileExistsError:
            pass

        utils = HalUtils(ext, remove_buses=True)

        addrmaps = utils.getAddrmapNodes(nodes[0], remove_root=False)

        if list_files:
            self.list_files(addrmaps, outdir, utils)
        else:
            for node in addrmaps:
                context = {
                        'node' : node,
                        'addrmap_nodes' : addrmaps
                        }
                text = utils.process_template(context, "addrmap.j2")
                out_file = os.path.join(outdir, utils.getTypeName(node) + ".h")
                with open(out_file, 'w') as f:
                    f.write(text)

            self.copy_base_headers(outdir)

