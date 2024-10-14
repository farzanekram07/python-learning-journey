def negativeNumbers():
    i = 0
    n = int(input("Enter the range:"))
    for i in range(i-n, i, 1):
        print(i)

negativeNumbers()


print("2nd Appraoch")

for num in range(-10, 0, 1):
    print(num)
    