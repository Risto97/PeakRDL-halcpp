#ifndef _ARCH_IO_H_
#define _ARCH_IO_H_

#include <cstdint>


class MemIoNode {
public:
    static inline uint32_t read32(uint32_t addr) { return *(volatile uint32_t*)addr; }

    template<typename DATA_T>
    static inline void write(uint32_t addr, DATA_T val) { *(volatile DATA_T*)addr = val; }

};

class ArchIoNode : public MemIoNode {
public:

};

#endif // !_ARCH_IO_H_
