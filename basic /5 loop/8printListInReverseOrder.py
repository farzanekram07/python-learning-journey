def reverseList(list):
    lst = []
    print("reversing the number of the list", end = " ")
    for i in range(1, len(list)+1):
        lst.append(list[-i])
        print(list[-i], end = " ")
    print()
    print("reversing list", lst)
list = [1, 2, 3, 4, 5]
reverseList(list)
