#ifndef _HALCPP_BASE_H_
#define _HALCPP_BASE_H_

#include <stdint.h>
#include <type_traits>

template <uint32_t START_BIT, uint32_t END_BIT, typename PARENT_TYPE>
class FieldNode {
private:
    using dataType =
        typename std::conditional<(END_BIT - START_BIT + 1) <= 8, uint8_t,
                                  typename std::conditional<(END_BIT - START_BIT + 1) <= 16,
                                                            uint16_t, uint32_t>::type>::type;

public:
    FieldNode(){};

    static constexpr uint32_t calc_mask() {
        static_assert(END_BIT <= 31, "Register cannot be bigger than 32 bits");
        return (~0u) ^ (((1u << (END_BIT - START_BIT + 1)) - 1) << START_BIT);
    }

    static inline void set(dataType val) {
        PARENT_TYPE::set((PARENT_TYPE::get() & calc_mask()) | (val << START_BIT));
    }

    static inline dataType get() {
        return ((PARENT_TYPE::get() & ~calc_mask()) >> START_BIT); 
    }

    // Operators
    template <typename T>
    void operator=(const T val) {
        static_assert(std::is_integral<T>::value, "T must be an integral type.");
        set(val);
    }
    template <typename T>
    inline operator const T() const {
        static_assert(std::is_integral<T>::value, "T must be an integral type.");
        static_assert(
            sizeof(T) >= (float)(END_BIT - START_BIT + 1) / 8,
            "T must be smaller than or equal to Field width, otherwise data will be lost");
        return static_cast<T>(get());
    }
    constexpr uint32_t get_abs_addr() { return PARENT_TYPE::get_abs_addr(); }
};

template <uint32_t BASE, typename PARENT_TYPE>
class RegNode {
public:
    RegNode() {}

    static inline uint32_t get() { return PARENT_TYPE::get(BASE); }
    static inline void set(uint32_t val) { PARENT_TYPE::set(BASE, val); }

    template<typename T>
    inline void operator=(const T &val) {
        static_assert(std::is_integral<T>::value, "T must be an integral type.");
        set(val);
    }

    template <typename T>
    inline operator const T() const {
        static_assert(std::is_integral<T>::value, "T must be an integral type.");
        return static_cast<T>(get());
    }

    constexpr uint32_t get_abs_addr() { return PARENT_TYPE::get_abs_addr() + BASE; }
};

template <uint32_t BASE, typename PARENT_TYPE>
class AddrmapNode {
public:
    AddrmapNode() {}

    static inline uint32_t get(const uint32_t addr) { return PARENT_TYPE::get(addr + BASE); }
    static inline void set(const uint32_t addr, uint32_t val) {
        PARENT_TYPE::set(addr + BASE, val);
    }
    constexpr uint32_t get_abs_addr() { return PARENT_TYPE::get_abs_addr() + BASE; }
};

template <uint32_t BASE, uint32_t SIZE, typename PARENT_TYPE>
class MemNode {
public:
    MemNode() {}

    static constexpr uint32_t base = BASE;
    static constexpr uint32_t size = SIZE;

    inline uint32_t get(const uint32_t addr) { return PARENT_TYPE::get(addr + BASE); }
    inline void set(const uint32_t addr, uint32_t val) { PARENT_TYPE::set(addr + BASE, val); }
    constexpr uint32_t get_abs_addr() { return PARENT_TYPE::get_abs_addr() + BASE; }
    constexpr uint32_t get_size() { return SIZE; }
};

template <typename D>
class ARCH_IO_NODE {
private:
    D& impl() { return *static_cast<D*>(this); }  // CRTP

public:
    static inline uint32_t read32(uint32_t addr) { return *(volatile uint32_t*)addr; }
    static inline void write32(uint32_t addr, uint32_t val) { *(volatile uint32_t*)addr = val; }
};

template <uint32_t BASE>
class TopNode : public ARCH_IO_NODE<TopNode<BASE>> {
public:
    TopNode() {}

public:
    constexpr uint32_t get_abs_addr() { return BASE; }

    static inline void set(uint32_t addr, uint32_t val) {
        ARCH_IO_NODE<TopNode<BASE>>::write32(addr + BASE, val);
    }
    static inline uint32_t get(uint32_t addr) { return ARCH_IO_NODE<TopNode<BASE>>::read32(addr + BASE); }
};

#endif
