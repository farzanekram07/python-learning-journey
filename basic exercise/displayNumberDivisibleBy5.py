def displayNumDivBy5(myList):
    newList = []
    for num in myList:
        if num % 5 == 0:
            newList.append(True)
        else:
            newList.append(False)
    return newList

List = [3, 10, 40, 33, 65]
print("original List: ", List)
print("matching: ", displayNumDivBy5(List))


#  EXAMPLE
