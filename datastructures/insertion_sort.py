def insertionSort( theSeq ):
    n = len (theSeq)
    for i in range (1,n):
        value = theSeq[i]
        pos = i
        while pos > 0 and value < theSeq[pos -1]:
            theSeq[pos] = theSeq[pos - 1]
            pos -=1
        theSeq[pos] = value


seq = [1,67,2,12,5]
print (seq)
insertionSort(seq)
print(seq)