def closest_number(n, m):
    if m == 0:
        return 0
    
    q = round(n / m)
    num1 = q * m

    # to handle both positive and negative
    if n * m > 0:  
        num2 = m * (q + 1)
    else:
        num2 = m * (q - 1)

    # to find which num is closest, num1 < num2
    if abs(n - num1) < abs(n - num2):  
        return num1
    elif abs(n - num1) > abs(n - num2):
        return num2
    elif abs(n - num1) == abs(n - num2):
        if abs(num1) > abs(num2):
            return num1
        else:
            return num2 

n = int(input())
m = int(input())
print(closest_number(n, m))
