#include <firebird-ttmath/ttmath.h>
#include <type_traits>
#include <iostream>

using Integer = ttmath::Int<TTMATH_BITS(128)>;
static_assert(sizeof(Integer) == 16, "Firebird INT128 size");
static_assert(alignof(Integer) <= 8, "Firebird descriptor alignment");
static_assert(std::is_trivial<Integer>::value, "Firebird union storage");

int main()
{
    Integer value, increment;
    value.FromString("12345678901234567890123456789012345678");
    increment = ttmath::sint(42);
    if (value.Add(increment))
        return 1;
    std::string text;
    value.ToString(text);
    if (text != "12345678901234567890123456789012345720")
        return 2;
    value = ttmath::sint(-8);
    value = value >> 2;
    value.ToString(text);
    if (text != "-2")
        return 3;
    std::cout << "Firebird INT128 layout, arithmetic and signed shifts passed\n";
}
