def printPrimeNumbers(start, end ):
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
start, end = map(int, input().split())
printPrimeNumbers(start, end)



# optimize it using math.sqrt