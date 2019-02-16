R = {"O": 0, "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
N = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L",
     40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}


def arabic(s):
    count = 1
    total = 0
    last = "O"
    s += "O"
    for l in s:
        if l == last:
            count += 1
        elif R[l] > R[last]:
            total -= count * R[last]
            count = 1
        else:
            total += count * R[last]
            count = 1
        last = l
    return total


def roman(n):
    out = []
    for i in sorted(N, reverse=True):
        c, n = divmod(n, i)
        out.append(N[i] * c)
    return "".join(out)


print(roman(7))
print(roman(49))
print(roman(120))
print(roman(1992))
print(roman(3888))
print(roman(2015))
print(arabic("VII"))
print(arabic("XLIX"))
print(arabic("CXX"))
print(arabic("MCMXCII"))
print(arabic("MMMDCCCLXXXVIII"))
print(arabic("MMXV"))
# 7 49 120 1992 3888 2015
