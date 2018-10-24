def binarySearch(theValues, target):
    low = 0
    high = len(theValues) -1
    while low <= high:
        mid = (low + high)//2
        if theValues[mid] == target:
            return True
        elif target < theValues[mid]:
            high = mid -1
        else:
            low = mid + 1
    return False


print (binarySearch([1,2,3,4,5,6,7,8,9], 8))

print (binarySearch([1,2,3,4,5,6,7,8,9], 8))
