def countDigit(number):
    count = 0
    while number != 0:
        number = number // 10
        count += 1
    return count

number = int(input())
print(countDigit(number))
        