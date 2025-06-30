def fibonacciSeries(n):
    n1 , n2 = map(int, input().split())
    for i in range(n):
        print(n1 , end = " ")
        n1, n2 = n2, n1 + n2
    print()
n = int(input())
fibonacciSeries(n)