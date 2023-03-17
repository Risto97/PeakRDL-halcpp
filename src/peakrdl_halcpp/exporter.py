from systemrdl import RDLWalker
from systemrdl.node import  Node, RootNode
from typing import List, Union
import os
import shutil

from .halutils import *

class HalExporter():
    def __init__(self):
        pass

    def export(self, nodes: 'Union[Node, List[Node]]', outdir: str, traverse: bool=False, **kwargs: 'Dict[str, Any]') -> None:

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

        walker = RDLWalker(unroll=True)
        listener = HalListener()
        walker.walk(nodes[0], listener)


        for node in listener.addrmaps:
            context = {
                    'node' : node,
                    'addrmap_nodes' : listener.addrmaps
                    }
            text = process_template(context, "addrmap.j2")
            out_file = os.path.join(outdir, getTypeName(node) + "_hal" + ".h")
            with open(out_file, 'w') as f:
                f.write(text)

        halcpp_base = os.path.join(os.path.dirname(__file__), "templates/halcpp_base.h")
        shutil.copy(halcpp_base, outdir)

