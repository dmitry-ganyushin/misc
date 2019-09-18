
class Solution:
    def __init__(self):
        pass

    def check(self, list1, list2):
        d1 = self.make_dict(list1)
        d2 = self.make_dict(list2)
        for k,v in d2.items():
            if k not in d1 or v > d1[k]:
                return False    
        return True 
    def make_dict(self, l):
        d={}
        for s in l:
            d[s] = d.setdefault(s, 0) +1
        return d


def main():
    s = Solution()
    print(s.check(["a", "a", "b", "c"], ["a", "b"]))
    print(s.check(["a", "a", "b", "c"], ["a", "b", "d"]))
    
if __name__ == "__main__":
    main()

