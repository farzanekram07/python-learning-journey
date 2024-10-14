def acceptListOfFiveFloatNumbers():
    list = []
    for i in range(5):
        num = float(input())
        list.append(num)
    return list

print(acceptListOfFiveFloatNumbers())
