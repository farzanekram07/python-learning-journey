def downwardHalfPyramid(n):
    for i in range(n):
        for j in range(i, n):
            print("*", end = " ")
        print()

n = int(input())
downwardHalfPyramid(n)