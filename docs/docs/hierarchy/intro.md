---
sidebar_position: 1
---

# Architecture

PeakRDL-halcpp is composed of C++ library of primitive template classes that correspond to SystemRDL components.
They can be found in [src/include](https://github.com/Risto97/PeakRDL-halcpp/tree/master/src/peakrdl_halcpp/include)

There you can find the following base template classes:
*   [AddrmapNode](/docs/hierarchy/nodes/addrmap)
*   [RegfileNode](/docs/hierarchy/nodes/regfile)
*   [RegNode](/docs/hierarchy/nodes/reg)
*   [FieldNode](/docs/hierarchy/nodes/field)
*   [MemNode](/docs/hierarchy/nodes/mem)
*   [ArchIoNode](/docs/hierarchy/nodes/arch_io)

The C++ template classes represent the components under the same name in SystemRDL standard.
The hierarchy stays the same, and its made by compositions of objects inside classes.
