import math
def find_gcd1(first_number, second_number):
    gcd = 1
    for i in range(1, min(first_number, second_number) + 1):
        if first_number % i == 0 and second_number % i == 0:
            gcd = i
    return gcd

def find_gcd2(a, b):
    get_gcd = math.gcd(a, b)
    return get_gcd

def find_gcd3(a, b):
    # Euclidean Algorithm
    '''GCD(a, b) = GCD(b, a % b)'''
    # This reduces the size of numbers very fast, 
    # making it super efficient even for large numbers.
    while b != 0:
        a, b = b, a % b
    return a

a, b = map(int, input("Enter space separated first and second number: ").split())
print(f"The gcd of {a} and {b} is :", find_gcd1(a, b))
print(f"The GCD of {a} and {b} using math.gcd is :", find_gcd2(a, b))
print(f"The GCD of {a} and {b} using Eucidean Algorithm:", find_gcd3(a, b))