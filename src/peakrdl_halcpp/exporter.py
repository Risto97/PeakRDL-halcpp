from systemrdl.node import  Node, RootNode
from typing import List, Union
import os
import shutil

from .halutils import *

class HalExporter():
    def __init__(self):
        pass

    def export(self,
            nodes: 'Union[Node, List[Node]]',
            outdir: str, 
            traverse: bool=False,
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

        for node in addrmaps:
            context = {
                    'node' : node,
                    'addrmap_nodes' : addrmaps
                    }
            text = utils.process_template(context, "addrmap.j2")
            out_file = os.path.join(outdir, utils.getTypeName(node) + "_hal" + ".h")
            with open(out_file, 'w') as f:
                f.write(text)

        halcpp_base = os.path.join(os.path.dirname(__file__), "templates/halcpp_base.h")
        shutil.copy(halcpp_base, outdir)

