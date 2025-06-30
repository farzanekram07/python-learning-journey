def printTable(start, end):
    for i in range(start, end):
        for j in range(start, end):
            print(i * j, end = "\t")
        print()

start, end = map(int, input("Enter start and end of the Table: ").split(","))
printTable(start, end)