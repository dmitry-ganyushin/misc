from bisect import bisect
intervals = [(8, 9), (1, 5), (6, 7),(10, 11)]
print(intervals)
intervals.sort(key=lambda r : r[0])
print(intervals)

def find_element(intervals, interval):
    """search by first element in tuple"""
    ind =bisect(intervals, interval)
    if (intervals[ind-1] == interval):
        return True
    else:
        return False

def find_element_binary(intervals, interval):
    """binary search for a pair of elements"""
    left = 0
    right = len(intervals) - 1
    found = False
    while left<=right and not found:
        middle = (left + right)//2
        if interval[0] > intervals[middle][0]:
            left = middle+1
        elif interval[0] < intervals[middle][0]:
            right = middle-1
        elif interval[0]== intervals[middle][0]:
            found = True
    if found:
        if interval[0]== intervals[middle][0] and interval[1]== intervals[middle][1]:
            return True
        else:
            return False


print(find_element(intervals, (10,11)) - 1)
print(find_element_binary(intervals, (10,11)))
