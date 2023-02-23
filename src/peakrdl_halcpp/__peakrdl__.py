from typing import TYPE_CHECKING

from .exporter import  HalExporter

if TYPE_CHECKING:
    import argparse
    from systemrdl.node import AddrmapNode


class Exporter:
    short_desc = "Generate CPP Hardware Abstraction Layer libraries"
    long_desc = "Generate CPP Hardware Abstraction Layer libraries"


    def add_exporter_arguments(self, arg_group: 'argparse.ArgumentParser') -> None:
        # arg_group.add_argument(
        #     "--logo",
        #     dest="logo",
        #     default=None,
        #     help="Logo to be insterted in the middle of the block"
        # )

        arg_group.add_argument(
            "--traverse",
            dest="traverse",
            default=False,
            action="store_true",
            help="Traverse and generate the whole hierarchy if True"
        )


    def do_export(self, top_node: 'AddrmapNode', options: 'argparse.Namespace') -> None:
        hal = HalExporter(
        )
        hal.export(
            top_node,
            options.output,
            options.traverse,
        )

