def multiplicationTable(n):
    i = 1
    while i <= 10:
        print(f"{n} * {i:<2}: {n * i:< 3}")
        i += 1

n = int(input("Enter the number: "))
multiplicationTable(n)


# {n * i:< 3} - ensuring result is left aligned 
#  at least  3 spaces