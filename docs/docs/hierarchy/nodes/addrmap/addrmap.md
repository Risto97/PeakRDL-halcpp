---
sidebar_position: 4
---
# AddrmapNode

`AddrmapNode` is a template class that represents an `addrmap` component in SystemRDL.<br/>
`AddrmapNode` can contain `RegNodes`, `MemNodes`, `RegFileNodes` and other `AddrmapNodes`, but an `AddrmapNode` can only be contained within another `AddrmapNode` or can be a top `AddrmapNode`.

## `AddrmapNode`

`AddrmapNode` template has the following declarations:

### `AddrmapNode` with `PARENT_TYPE`

The following template is a general `AddrmapNode` which expect to be contained within another `AddrmapNode`.
In case of `read`, `write` requests to this node, the requests will be forwarded to the containing node, as this node does not implement memory IO operations.

This template expects 2 parameters:
*   `BASE` is an address offset within containing `AddrmapNode`.
*   `PARENT_TYPE` is a type of the parent `AddrmapNode`, a specialization of the `AddrmapNode` where `PARENT_TYPE==void` is provided [below](#top_addrmap).

```cpp
template <uint32_t BASE, typename PARENT_TYPE = void>
class AddrmapNode;
```

### Top `AddrmapNode` {#top_addrmap}

A special case of `AddrmapNode` is an addrmap node that is not contained within another `AddrmapNode`, but instead it implements the memory IO operations, and it ends the (getter, setter) call chain from lower levels of hierarchy.
It has the following declaration:

```cpp
template <uint32_t BASE>
class AddrmapNode <BASE, void> : public ArchIoNode;
```

As you can see it is a specialization of `AddrmapNode` where the `PARENT_TYPE==void`.
The `BASE` parameter is the same.

In addition, the top `AddrmapNode` inherits an [`ArchIoNode`](/docs/hierarchy/nodes/arch_io), which is a class that provides memory IO operations of the platform.<br/>
`ArchIoNode` is expected to implement `write32()` and `read32()` methods.
