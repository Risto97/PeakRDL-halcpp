#ifndef _HALCPP_UTILS_H_
#define _HALCPP_UTILS_H_

#include <type_traits>

namespace halcpp{
template <class LIB, class = void>
struct node_has_set : std::false_type {};

template <class LIB>
struct node_has_set<LIB,
                    std::enable_if_t<std::is_invocable_r<bool, decltype(LIB::has_set)>::value>>
    : std::integral_constant<bool, LIB::has_set()> {};

template <class LIB>
constexpr bool node_has_set_v = node_has_set<LIB>::value;

template <class LIB, class = void>
struct node_has_get : std::false_type {};

template <class LIB>
struct node_has_get<LIB,
                    std::enable_if_t<std::is_invocable_r<bool, decltype(LIB::has_get)>::value>>
    : std::integral_constant<bool, LIB::has_get()> {};

template <class LIB>
constexpr bool node_has_get_v = node_has_get<LIB>::value;
}

#endif // !_HALCPP_UTILS_H_
