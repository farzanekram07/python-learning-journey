def sumOfSeries(n, k):
    sum = 0
    for i in range(0, n):
        print(k, end = "+")
        sum = sum + k
        k = (k * 10)  + 2
    return sum

n, k = map(int, input().split(","))
print(sumOfSeries(n, k))

