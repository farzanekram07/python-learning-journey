def powerOfExponent(base, exponent):
    res = 1
    for i in range(exponent):
        res = res * base
    return res

base, exponent = map(int, input("Enter the base and exponent comma separated: ").split(","))
print(powerOfExponent(base, exponent))