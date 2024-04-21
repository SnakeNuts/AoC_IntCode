def get_digit(number, n):
    return number // 10**n % 10


value = 99

# A = value // 10000
# value = value - A * 10000
# B = value // 1000
# value = value - B * 1000
# C = value // 100
# value = value - C * 100
# D = value // 10
# value = value - D * 10
# E = value // 1

A = get_digit(value, 4)
B = get_digit(value, 3)
C = get_digit(value, 2)
D = get_digit(value, 1)
E = get_digit(value, 0)

print(f"{A},{B},{C},{D},{E}")
