#ifndef _ADDRMAP_NODE_H_
#define _ADDRMAP_NODE_H_

#include "arch_io.h"
#include <cstdint>

// TODO define architecture type size, so it replaces uint32_t

template <uint32_t BASE, typename PARENT_TYPE = void>
class AddrmapNode {
public:
    static constexpr uint32_t get_abs_addr() { return PARENT_TYPE().get_abs_addr() + BASE; }

    // TODO uint32_t should not be fixed
    static inline uint32_t get(const uint32_t addr) { return PARENT_TYPE::get(addr + BASE); }

    template<typename DATA_T>
    static inline void set(const uint32_t addr, DATA_T val) {
        PARENT_TYPE::set(addr + BASE, val);
    }
};

/* Specialization for the Top hierarchy addrmap
 *  Top node does not have a parent.
 *  Insted it inherits ArchIoNode, that implements memory access for architecture
 */
template <uint32_t BASE>
class AddrmapNode <BASE, void> : public ArchIoNode {
public:

    static constexpr uint32_t get_abs_addr() { return BASE; }

    template<typename DATA_T>
    static inline void set(uint32_t addr, DATA_T val) {
        ArchIoNode::write(addr + BASE, val);
    }
    // TODO uint32_t should not be fixed
    static inline uint32_t get(uint32_t addr) { return ArchIoNode::read32(addr + BASE); }
};

#endif // !_ADDRMAP_NODE_H_
