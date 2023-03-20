#ifndef _ARCH_IO_H_
#define _ARCH_IO_H_

#include <cstdint>

class ArchIoNode {
public:
    static inline uint32_t read32(uint32_t addr) { return *(volatile uint32_t*)addr; }
    static inline void write32(uint32_t addr, uint32_t val) { *(volatile uint32_t*)addr = val; }
};

#endif // !_ARCH_IO_H_
