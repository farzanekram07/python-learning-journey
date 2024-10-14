def oddIndexElementsFromList(list):
    for i in range(len(list)):
        if i % 2 == 1:
            print(list[i], end = " ")

    print()

list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
oddIndexElementsFromList(list)