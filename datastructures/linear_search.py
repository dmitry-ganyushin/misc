mylist=[23,65,23,56,34]

def linearSearch(theValues, target):
    n = len (theValues)
    for i in  range(n):
        if theValues[i]==target:
            return True
    return False

print ("23 in mylist is" + str(linearSearch(mylist, 23)))

