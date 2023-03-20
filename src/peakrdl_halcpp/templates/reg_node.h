#ifndef _REG_NODE_H_
#define _REG_NODE_H_

#include <stdint.h>
#include <type_traits>
#include "halcpp_utils.h"

namespace halcpp{

template <uint32_t BASE, uint32_t WIDTH, typename PARENT_TYPE>
class RegBase {
public:
    RegBase() {}

    constexpr uint32_t get_abs_addr() { return PARENT_TYPE::get_abs_addr() + BASE; }

protected:
    static constexpr uint32_t width = WIDTH;
    static constexpr uint32_t rel_base = BASE;
    using parent_type = PARENT_TYPE;
    using dataType =
        typename std::conditional<WIDTH <= 8, uint8_t,
                                  typename std::conditional<WIDTH <= 16,
                                                            uint16_t, uint32_t>::type>::type;
};

template<typename BASE_TYPE>
class RegWrMixin : public BASE_TYPE {
public:
    using parent = typename BASE_TYPE::parent_type;
    static constexpr bool has_set() { return true; };

    static inline void set(typename BASE_TYPE::dataType val) {
        parent::set(BASE_TYPE::rel_base, val);
    }

    // Dont bother with operator= equal as its going to be overriden by inherited class anyways

    RegWrMixin() {}
};

template <typename BASE_TYPE>
class RegRdMixin : public BASE_TYPE {
private:
    using parent = typename BASE_TYPE::parent_type;

public:
    static constexpr bool has_get() { return true; };

    static typename BASE_TYPE::dataType get() {
        return parent::get(BASE_TYPE::rel_base);
    }

    template <typename T>
    inline operator const T() {
        static_assert(std::is_integral<T>::value, "T must be an integral type.");
        static_assert(
            sizeof(T) >= (float)(BASE_TYPE::width / 8),
            "T must be smaller than or equal to Field width, otherwise data will be lost");
        return static_cast<T>(get());
    }
    RegRdMixin() {}
};

// TODO merge this with FieldNode ???
template <typename... RegMixins>
class RegNode : public RegMixins... {
private:
    template <typename T>
    void call_set([[maybe_unused]] typename T::dataType val) {         // Find a way to ignore warning -Wunused-but-set-parameter
        if constexpr (node_has_set_v<T>) T::set(val);
    }
    template <typename T, typename T1, typename... Ts>
    void call_set(typename T::dataType val) {
        call_set<T>(val);
        call_set<T1, Ts...>(val);
    }

public:
    template <typename Tp, typename T = void>
    typename std::enable_if<std::disjunction_v<node_has_set<RegMixins>...>, T>::type
    operator=(Tp val) {
        static_assert(std::is_integral<Tp>::value, "T must be an integral type.");
        call_set<RegMixins...>(val);
    }
    RegNode() {}
};

template <uint32_t BASE, uint32_t WIDTH, typename PARENT_TYPE>
using RegRO = RegNode<RegRdMixin< RegBase< BASE, WIDTH, PARENT_TYPE> > >;

template <uint32_t BASE, uint32_t WIDTH, typename PARENT_TYPE>
using RegWO = RegNode<RegWrMixin< RegBase< BASE, WIDTH, PARENT_TYPE> > >;

template <uint32_t BASE, uint32_t WIDTH, typename PARENT_TYPE>
using RegRW = RegNode<RegWrMixin< RegBase< BASE, WIDTH, PARENT_TYPE> >, RegRdMixin< RegBase< BASE, WIDTH, PARENT_TYPE> >  >;

}

#endif // !_REG_NODE_H_
