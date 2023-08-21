---
sidebar_position: 6
---
# ArchIoNode

This node is meant to provide the memory IO operation of the platform.
It is supposed to implement `write32` and `read32` methods.

`ArchIoNode` is meant to be inherited by a top `AddrmapNode`.

By default a default `ArchIoNode` is provided and will be copied to the output directory.
The default node provides a typical memory IO operations for a CPU.
However it is possible to override this node in cases of:
*   Using generated halcpp drivers as a `UVM-RAL` for `SystemC-UVM` or `C++` testbenches.
*   For debugging, where you might want to replace memory IO with console prints
*   For Emulation, where you might want to model memory IO operations its side effects in the platform.
*   Or Simply if the provided `ArchIoNode` is not adequate.

## Overriding `ArchIoNode`

In order to override the default class the easiest way to do it is following:

```cpp
#define _ARCH_IO_H_

class ArchIoNode {
public:
// ... Your custom implementation
};

#include "soc_hal.h"
```

The easiest solution is to define macro `_ARCH_IO_H_` before including the HAL driver header file (in this case `soc_hal.h`).
After that you need to provide your custom implemetnation for ArchIoNode.
