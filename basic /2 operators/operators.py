# arithmetic operators
a = 15
b = 4
# addition
print("Addition:", a + b)  
# subtraction
print("Subtraction:", a - b) 
# multiplication
print("Multiplication:", a * b)  
# division
print("Division:", a / b) 
# floor division
print("Floor Division:", a // b)  
# modulus
print("Modulus:", a % b) 
# exponentiation
print("Exponentiation:", a ** b)


# comparision operators
a = 13
b = 33
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)


# logical operators with boolean
a = True
b = False
print(a and b)
print(a or b)
print(not a)
# but python has a facility to operate with number also
''' python's Rule for and:
    A and B returns:
    B if A is truthy
    A if A is falsy '''
# example
print(0 and 3)   # → 0 (because 0 is falsy)
print(3 and 0)   # → 0 (because 3 is truthy, so return 0)
print(3 and 7)   # → 7 (both truthy, so return second)
print(0 and 0)   # → 0 (first is falsy, so return first)
''' python's rule for or:
    A or B returns:
    A if A is truthy
    B if A is falsy '''
# example
print(5 or 3)  # → 5 (first is truthy, return it)
print(0 or 3)  # → 3 (first is falsy, return second)
''' python's rule for not:
    not A returns:
    True if A is falsy
    False if A is truthy '''
# example
print(not 5)     # → False  (5 is truthy)
print(not 0)     # → True   (0 is falsy)
print(not "")    # → True   (empty string is falsy)
print(not "hi")  # → False  (non-empty string is truthy)


# bitwise operators
a = 10
b = 4
print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)


# assignment operators
a = 10
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)


# identity operators
''' is          True if the operands are identical 
    is not      True if the operands are not identical '''
a = 10
b = 20
c = a
print(a is not b)
print(a is c)


# membership operators
''' in            True if value is found in the sequence
    not in        True if value is not found in the sequence '''
x = 24
y = 20
list = [10, 20, 30, 40, 50]
if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")
if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")


# ternary operator
''' Syntax :  [on_true] if [expression] else [on_false] '''
a, b = 10, 20
min = a if a < b else b
print(min)


# precedence and associativity of operators 
# operator precedence
expr = 10 + 20 * 30
print(expr)
name = "Alex"
age = 0
if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")
# operator associativity
print(100 / 10 * 10)
print(5 - 2 + 3)
print(5 - (2 + 3))
print(2 ** 3 ** 2)

# recommended problems
#1. Code to implement basic arithmetic operations on integers
num1 = 5
num2 = 2
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2
remainder = num1 % num2
print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)
print("Remainder:", remainder)

#2. Code to implement Comparison operations on integers
num1 = 30
num2 = 35
if num1 > num2:
    print("The first number is greater.")
elif num1 < num2:
    print("The second number is greater.")
else:
    print("The numbers are equal.")



