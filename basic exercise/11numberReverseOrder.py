def reverse(num):
    reverse = 0
    while(num > 0):
        temp = num % 10
        reverse = (reverse * 10) + temp 
        num = num // 10

    return reverse

num = 12345
print(reverse(num))