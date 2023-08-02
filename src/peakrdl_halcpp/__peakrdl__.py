from systemrdl.node import  AddrmapNode

from peakrdl.plugins.exporter import ExporterSubcommandPlugin #pylint: disable=import-error
from peakrdl.config import schema #pylint: disable=import-error

from peakrdl.main import main as peakrdl_main
from .exporter import  HalExporter
import sys
import argparse

class Exporter(ExporterSubcommandPlugin):
    short_desc = "Generate CPP Hardware Abstraction Layer libraries"
    long_desc = "Generate CPP Hardware Abstraction Layer libraries"

    hal = None


    def add_exporter_arguments(self, arg_group: 'argparse.ArgumentParser') -> None:

        arg_group.add_argument(
                "--ext",
                nargs="*", 
                default=[],
                help="list of addrmap modules that have implemented <name>_EXT class in <name>_ext.h header file, used for extending functionality"
                )

        arg_group.add_argument(
            "--list-files",
            dest="list_files",
            default=False,
            action="store_true",
            help="Dont generate files, but instead just list the files that will be generated, and external files that need to be included"
        )

        arg_group.add_argument(
            "--keep-buses",
            dest="keep_buses",
            default=False,
            action="store_true",
            help="If there is an addrmap containing only addrmaps, not registers, by default it will be ommited in hierarchy, it is possible to keep it by passing --keep-buses flag"
        )


    def do_export(self, top_node: 'AddrmapNode', options: 'argparse.Namespace') -> None:
        if Exporter.hal is None:            # Use static member so the hal object is the same on the next pass for zicsr registers
            Exporter.hal = HalExporter(
                    outdir=options.output,
                    ext=options.ext,
                    )
            Exporter.hal.create_model(top_node)
        elif Exporter.hal.top is not None and "USE_ZICSR=1" in options.defines:
            Exporter.hal.halutils.add_csr_addrmaps(top_node, Exporter.hal.top, Exporter.hal.keep_buses)

        if "-DUSE_ZICSR=1" not in sys.argv:
            sys.argv.append("-DUSE_ZICSR=1")
            peakrdl_main()

        if options.list_files:
            Exporter.hal.list_files()
            exit()
        else:
            Exporter.hal.generate_output()
            exit()

