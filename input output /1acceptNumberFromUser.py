def userInput():
    n, m = map(int, input("Enter two input from the user: ").split(" "))
    multiplication = n * m
    return multiplication

print(userInput())
