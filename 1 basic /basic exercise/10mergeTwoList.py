def mergeList(list1, list2):
    list = []
    for i in list1:
        if i%2 == 1:
            list.append(i)
        
    for i in list2:
        if i % 2 == 0:
            list.append(i)

    return list

list1 = [1, 2, 3, 4, 5, 6]
list2 = [7, 8, 9, 10, 11, 12]
print(mergeList(list1, list2))
