def printPattern(n):
    for i in range(n + 1):
        for j in range(n-i, 0, -1):
            print(j, end = " ")
        print()

n = int(input())
printPattern(n)