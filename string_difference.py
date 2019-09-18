# Given two strings (lower case a->z) determine how many characters we need to remove (from  either)
# to make them anagrams?
# EXAMPLE : hello, billion --> answer 6
#  
#

class Solution:
    NUMBER_LETTERS = 26
    def __init__(self, s1, s2):
        c1 = self.getCharCounts(s1)
        c2 = self.getCharCounts(s2)
        print(self.getDelta(c1, c2))
    def getDelta(self, array1, array2):
        delta = 0
        for i in range (0, len(array1)):
            delta += abs(array1[i] - array2[i])
        return delta
 

    def getCharCounts(self, string):
        charCounts = [0 for _ in range(0, self.NUMBER_LETTERS)]
        offset = ord('a')
        for s in string:
            charCounts[ord(s) - offset] += 1 
        return charCounts

def main():
    s1 = "hello"
    s2 = "billion"
    delta = Solution(s1, s2)
    print(delta)

if __name__ == "__main__":
    main()