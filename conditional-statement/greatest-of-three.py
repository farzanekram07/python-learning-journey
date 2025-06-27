#User function Template for python3
# Take a, b and c input and print the greatest of three
a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
elif c >= a and c >= b:
    print(c)
