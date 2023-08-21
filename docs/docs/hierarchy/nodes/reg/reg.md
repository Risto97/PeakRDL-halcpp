---
sidebar_position: 3
---
# RegNode

`RegNode` is a template class that represents a `reg` component in SystemRDL.<br/>
`RegNode` can contain only `FieldNodes`, and it must be instantiated within `AddrmapNode` (or `RegFileNode` TODO)

## `RegBase`

`RegBase` is a base class providing `constexpr` constants for basic information about the register.
The base class does not provide any `write` or `read` capabilities.

It is a template that takes the following template arguments

```cpp
template <uint32_t BASE, uint32_t WIDTH, typename PARENT_TYPE>
class RegBase {
```

The template parameters are:
*   `BASE` is a address offset within an `AddrmapNode`.
*   `WIDTH` is a width of the register.
*   `PARENT_TYPE` accepts a specialization of a `AddrmapNode` template, and is the type of the containing addrmap.
It is necessary to pass this type, because the `write` and `read` methods of the field will pass these requests to the parent register, along with the value written.


## `RegRdMixin` and `RegWrMixin`

Since the `RegBase` class does not provide any `write` or `read` capabilities, these two `Mixins` are supposed to provide the additional capabilities to the registers.
They are supposed to provide `setters` and `getters` for the registers, along with operator overloads.
The memory access is not done by these mixins, but the requests are instead passed to the addrmap nodes.

### Register access methods

The 2 mixins will provide at least the `get()` and `set()` methods for accessing the register.

## `RegNode`

`RegNode` is a template class is inheriting the parameter pack of mixins. The prototype is as shown:
```cpp
template <typename... RegMixins>
class RegNode : public RegMixins...
```

In order to provide Register that have `Read`, `Write` or `ReadWrite` capabilites, the template `RegNode` is inheriting parameter pack of `Mixins` meant to provide the additional functionality.

For example:
*   `RegNode` inheriting only `RegRdMixin` will be a `read-only` register.
*   `RegNode` inheriting only `RegWrMixin` will be a `write-only` register.
*   `RegNode` inheriting both `RegWrMixin` and `RegRdMixin` will be a `read-write` register.

In order to ease the use of these templates, common specializations of `RegNode` is already provided under the names:

###  `RegRO`
is a `read-only` field with a declaration:

```cpp
template <uint32_t BASE, uint32_t WIDTH, typename PARENT_TYPE>
using RegRO = ...
```

###  `FieldWO` 
is a `write-only` field with a declaration:

```cpp
template <uint32_t BASE, uint32_t WIDTH, typename PARENT_TYPE>
using RegWO = ...
```

### `FieldRW`
is a `read-write` field with a declaration:

```cpp
template <uint32_t BASE, uint32_t WIDTH, typename PARENT_TYPE>
using RegRW = ...
```

It is adviced to use these specializations to construct your registers
