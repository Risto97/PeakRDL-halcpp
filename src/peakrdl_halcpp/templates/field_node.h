#ifndef _FIELD_NODE_H_
#define _FIELD_NODE_H_

#include <stdint.h>
#include <type_traits>
#include "halcpp_utils.h"

namespace halcpp{

template <uint32_t START_BIT, uint32_t END_BIT, typename PARENT_TYPE>
class FieldBase {
public:
    FieldBase() {}

    static constexpr uint32_t get_abs_addr() { return PARENT_TYPE().get_abs_addr();}

protected:
    using parent_type = PARENT_TYPE;
    static constexpr uint32_t start_bit = START_BIT;
    static constexpr uint32_t end_bit = END_BIT;
    static constexpr uint32_t width = END_BIT-START_BIT+1;
    using dataType =
        typename std::conditional<width  <= 8, uint8_t,
                                  typename std::conditional<width <= 16,
                                                            uint16_t, uint32_t>::type>::type;

    static constexpr uint32_t calc_mask() {
        static_assert(width <= 32, "Register cannot be bigger than 32 bits");
        return (~0u) ^ (((1u << (width)) - 1) << START_BIT);
    }
};

template <typename BASE_TYPE>
class FieldWrMixin : public BASE_TYPE {
public:
    using parent = typename BASE_TYPE::parent_type;
    static constexpr bool has_set() { return true; };

    static inline void set(typename BASE_TYPE::dataType val) {
        if constexpr (node_has_get_v<parent>)
            parent::set((parent::get() & BASE_TYPE::calc_mask()) | (val << BASE_TYPE::start_bit));
        else
            parent::set(val << BASE_TYPE::start_bit);
    }

    template<uint32_t CONST_WIDTH, uint32_t CONST_VAL>
    static inline void set(const Const<CONST_WIDTH, CONST_VAL> &a){
        static_assert(CONST_WIDTH == BASE_TYPE::width, "Constant is not the same width as field");
        set((typename BASE_TYPE::dataType) a.val);
    }

    // Dont bother with operator= equal as its going to be overriden by inherited class anyways
    FieldWrMixin() {}
};

template <typename BASE_TYPE>
class FieldRdMixin : public BASE_TYPE {
private:
    using parent = typename BASE_TYPE::parent_type;

public:
    static constexpr bool has_get() { return true; };

    static typename BASE_TYPE::dataType get() {
        return (parent::get() & ~BASE_TYPE::calc_mask()) >> BASE_TYPE::start_bit;
    }

    template <typename T>
    inline operator const T() {
        static_assert(std::is_integral<T>::value, "T must be an integral type.");
        static_assert(
            sizeof(T) >= (float)(BASE_TYPE::end_bit - BASE_TYPE::start_bit + 1) / 8,
            "T must be smaller than or equal to Field width, otherwise data will be lost");
        return static_cast<T>(get());
    }
    FieldRdMixin() {}
};

// TODO merge this with RegNode ???
template <typename... FieldMixins>
class FieldNode : public FieldMixins... {
private:
    template <typename DT, typename T>
    void call_set([[maybe_unused]] const DT &val) const {         // Find a way to ignore warning -Wunused-but-set-parameter
        if constexpr (node_has_set_v<T>) T::set(val);
    }
    template <typename DT, typename T, typename T1, typename... Ts>
    void call_set(const DT val) const {
        call_set<DT, T>(val);
        call_set<DT, T1, Ts...>(val);
    }

public:
    template <typename Tp, typename T = void>
    typename std::enable_if<std::disjunction_v<node_has_set<FieldMixins>...>, T>::type
    operator=(Tp val) {
        call_set<Tp, FieldMixins...>(val);
    }
    FieldNode() {}
};

template <uint32_t START_BIT, uint32_t END_BIT, typename PARENT_TYPE>
using FieldRO = FieldNode<FieldRdMixin< FieldBase< START_BIT, END_BIT, PARENT_TYPE> > >;

template <uint32_t START_BIT, uint32_t END_BIT, typename PARENT_TYPE>
using FieldWO = FieldNode<FieldWrMixin< FieldBase< START_BIT, END_BIT, PARENT_TYPE> > >;

template <uint32_t START_BIT, uint32_t END_BIT, typename PARENT_TYPE>
using FieldRW = FieldNode<FieldWrMixin< FieldBase< START_BIT, END_BIT, PARENT_TYPE> >, FieldRdMixin< FieldBase< START_BIT, END_BIT, PARENT_TYPE> >  >;

}

#endif
