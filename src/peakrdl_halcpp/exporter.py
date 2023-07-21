from systemrdl.node import  Node, RootNode, AddrmapNode
import jinja2
from typing import List, Union, Any
import os
import shutil

from .haladdrmap import *
from .halutils import HalUtils

class HalExporter():
    def __init__(self,
                outdir : str,
                keep_buses : bool=False,
                ext : list=[],
                ):
        self.cpp_dir = "include"

        self.base_headers = [
                "halcpp_base.h",
                "halcpp_utils.h",
                "field_node.h",
                "reg_node.h",
                "csr_reg_node.h",
                "reg_arr_node.h",
                "addrmap_node.h",
                "arch_io.h",
                ]

        self.halutils = HalUtils(ext)

        self.top = None
        self.outdir = outdir
        self.keep_buses = keep_buses

    def list_files(self):
        assert self.top is not None
        out_files = [os.path.join(self.outdir, addrmap.type_name + ".h") for addrmap in self.top.get_addrmaps_recursive()]
        out_files += [os.path.join(self.outdir, x) for x in self.base_headers] + out_files
        print(*out_files) # Print files to stdout

    def copy_base_headers(self, outdir):
        abspaths = [os.path.join(os.path.dirname(__file__), self.cpp_dir, x) for x in self.base_headers]
        outdir = os.path.join(outdir, "include")
        if not os.path.exists(outdir):
            os.makedirs(outdir)
        [shutil.copy(x, outdir) for x in abspaths]

    def create_model(self, node: AddrmapNode) -> HalAddrmap:

        top = self.halutils.build_hierarchy(
                node=node,
                remove_root=False, # TODO fix
                keep_buses=self.keep_buses,
                )

        self.top = top
        return top
    
    def generate_output(self):
        assert self.top is not None
        try:
            os.makedirs(self.outdir)
        except FileExistsError:
            pass

        for halnode in self.top.get_addrmaps_recursive():
            context = {
                    'halnode'  : halnode,
                    'halutils' : self.halutils,
                    }
            text = self.process_template(context)
            out_file = os.path.join(self.outdir, halnode.type_name + ".h")
            with open(out_file, 'w') as f:
                f.write(text)

        self.copy_base_headers(self.outdir)

    def process_template(self, context : dict) -> str:

        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader('%s/templates/' % os.path.dirname(__file__)),
            trim_blocks=True,
            lstrip_blocks=True)

        env.filters.update({
            'zip' : zip,
            })

        res = env.get_template("addrmap.j2").render(context)
        return res

