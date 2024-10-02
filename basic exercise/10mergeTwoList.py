def mergeList(list1, list2):
    list = []
    for i in list1:
        if i % 2 == 1:
            list.append(i)

    for i in list2:
        if i % 2 == 0:
            list.append(i)

    return list

list1 = [10, 11, 12, 13]
list2 = [14, 15, 16, 17]
print(mergeList(list1, list2))

