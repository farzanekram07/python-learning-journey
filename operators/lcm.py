import math

def lcm(a, b):
    # LCM(a,b)= a×b / GCD(a,b)
    return abs(a * b) // math.gcd(a, b)

print(lcm(4, 6))  # Output: 12

# Without Using Built-in GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm1(a, b):
    return abs(a * b) // gcd(a, b)

print(lcm1(4, 6))  # Output: 12
