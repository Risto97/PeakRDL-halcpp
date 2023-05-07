#ifndef _REG_ARR_NODE_H_
#define _REG_ARR_NODE_H_

#include <stdint.h>
#include <type_traits>
#include "halcpp_utils.h"

namespace halcpp{

template <uint32_t BASE, uint32_t WIDTH, uint32_t LEN, uint32_t STRIDE, typename PARENT_TYPE>
class ArrRegBase {
public:

    static constexpr uint32_t get_abs_addr() { return PARENT_TYPE().get_abs_addr() + BASE; }

protected:
    static constexpr uint32_t width = WIDTH;
    static constexpr uint32_t rel_base = BASE;
    static constexpr uint32_t len = LEN;
    static constexpr uint32_t stride = STRIDE;
    using parent_type = PARENT_TYPE;
    using dataType =
        typename std::conditional<WIDTH <= 8, uint8_t,
                                  typename std::conditional<WIDTH <= 16,
                                                            uint16_t, uint32_t>::type>::type;
    using idxType =
        typename std::conditional<LEN <= 8, uint8_t,
                                  typename std::conditional<LEN <= 16,
                                                            uint16_t, uint32_t>::type>::type;
};

template<typename BASE_TYPE>
class ArrRegWrMixin : public BASE_TYPE {
public:
    using parent = typename BASE_TYPE::parent_type;
    static constexpr bool has_set() { return true; };

    static inline void set(typename BASE_TYPE::idxType idx, typename BASE_TYPE::dataType val) {
        if(idx >= BASE_TYPE::len)
            idx = BASE_TYPE::len-1;
        parent::set(BASE_TYPE::rel_base + (BASE_TYPE::width/8)*idx, val);
    }

    template<uint32_t CONST_WIDTH, uint32_t CONST_VAL>
    static inline void set(typename BASE_TYPE::idxType idx, const Const<CONST_WIDTH, CONST_VAL> &a){
        static_assert(BASE_TYPE::width == CONST_WIDTH, "You need to provide all the bits for concatenation.");
        if(idx >= BASE_TYPE::len)
            idx = BASE_TYPE::len-1;
        parent::set(BASE_TYPE::rel_base + (BASE_TYPE::width/8)*idx, a.val);
    }
};

template <typename BASE_TYPE>
class ArrRegRdMixin : public BASE_TYPE {
private:
    using parent = typename BASE_TYPE::parent_type;

public:
    static constexpr bool has_get() { return true; };

    static typename BASE_TYPE::dataType get(typename BASE_TYPE::idxType idx) {
        if(idx >= BASE_TYPE::len)
            idx = BASE_TYPE::len-1;
        return parent::get(BASE_TYPE::rel_base + (BASE_TYPE::width/8) * idx);
    }
};

// TODO merge this with FieldNode ???
template <typename... RegMixins>
class ArrRegNode : public RegMixins... {
};

template <uint32_t BASE, uint32_t WIDTH, uint32_t LEN, uint32_t STRIDE, typename PARENT_TYPE>
using ArrRegRO = ArrRegNode<ArrRegRdMixin< ArrRegBase< BASE, WIDTH, LEN, STRIDE, PARENT_TYPE> > >;

template <uint32_t BASE, uint32_t WIDTH, uint32_t LEN, uint32_t STRIDE, typename PARENT_TYPE>
using ArrRegWO = ArrRegNode<ArrRegWrMixin< ArrRegBase< BASE, WIDTH, LEN, STRIDE, PARENT_TYPE> > >;

template <uint32_t BASE, uint32_t WIDTH, uint32_t LEN, uint32_t STRIDE, typename PARENT_TYPE>
using ArrRegRW = ArrRegNode<ArrRegWrMixin< ArrRegBase< BASE, WIDTH, LEN, STRIDE, PARENT_TYPE> >, ArrRegRdMixin< ArrRegBase< BASE, WIDTH, LEN, STRIDE, PARENT_TYPE> >  >;

}

#endif // !_REG_ARR_NODE_H_


