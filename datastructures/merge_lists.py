#merge tow lists
def mergeSortedLists(listA, listB):
    newList = list()
    a = 0;
    b = 0;

    while a < len (listA) and b < len(listB):
        if listA[a] < listB[b]:
            newList.append(listA[a])
            a+=1
        else:
            newList.append(listB[b])
            b+=1

    # add the rest
    while a < len(listA):
        newList.append(listA[a])
        a+=1
    while b < len (listB):
        newList.append(listB[b])
        b+=1
    return newList
    
list1 = [4,6,7,9]
list2 = [1,2,5,7,8,9]

print(list1)
print(list2)

print(mergeSortedLists(list1, list2))