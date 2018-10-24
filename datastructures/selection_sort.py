#selection sort
def selectionSort(theSeq):
    n = len (theSeq)
    for i in range (n-1):
        smallNdx = i
        for j in range (i + 1, n):
            if theSeq[j] < theSeq[smallNdx]:
                smallNdx = j
        if smallNdx != i:
            theSeq[i], theSeq[smallNdx] = theSeq[smallNdx], theSeq[i]

seq = [5,2,6,2,6,78]
print(seq)
selectionSort(seq)
print (seq)