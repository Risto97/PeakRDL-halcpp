from systemrdl import RDLCompiler
from systemrdl.node import FieldNode, Node, RootNode, AddressableNode, RegNode, SignalNode
import jinja2
from typing import List, Union
import os

def num_of_fields(iter):
    return sum(1 for _ in iter)

def bit_mask(low, high, width=32, inverted=False ):
    vector = 0 
    for i in range(low, high+1):
        vector = vector | (2**i)
    if inverted:
        vector = (2**width-1) ^ vector
    return hex(vector) 


class HalExporter():
    def __init__(self):
        # self.flat_nodes = []
        pass

    def traverse(self, node : Node):
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

        context = {
                'top' : nodes[0],
                'bit_mask' : bit_mask,
                'len' : num_of_fields

                }
        out = self.gen_file(context)

        out_file = os.path.join(outdir, nodes[0].inst_name + "_hal" + ".h")
        with open(out_file, 'w') as f:
            f.write(out)



    def gen_file(self, context) -> str:

        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader('%s/templates/' % os.path.dirname(__file__)),
            trim_blocks=True,
            lstrip_blocks=True)

        res = env.get_template("halcpp.j2").render(context)
        return res
