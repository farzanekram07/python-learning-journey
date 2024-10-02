def pattern(n):
    for i in range(1, n):
        for j in range(i):
            print(i, end = " ")    
        print()
n = 5
pattern(n)