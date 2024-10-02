def palindrome(num):
    originalNum = num
    new = 0
    while(num > 0):
        print("original value is:", num)
        temp1 = num % 10
        print("after modulation value is :", temp1)
        new = (new * 10) + temp1
        print("adding modulation value to new value is:", new)
        num = num // 10
        print("rest value is:",(num))
        print()

    if originalNum == new:
        print("y")
    else:
        print("n")
num = 12321
palindrome(num)