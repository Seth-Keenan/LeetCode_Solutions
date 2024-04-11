class Solution:
    #Most issues with strings can be solved by thinking about how it would effect the problem if it was sorted
    #The syntax to remember this is important but weird to remember
    # ''.join(sorted())
    def isAnagramSort(self, s: str, t: str) -> bool:
        s_sort = ''.join(sorted(s))
        t_sort = ''.join(sorted(t))

        if s_sort == t_sort:
            return True
        else:
            return False

    def isAnagram(self, s: str, t: str) -> bool:
            sDict = {}

            if len(s) != len(t):
                return False

            for c in s:
                sDict[c] = sDict.get(c,0) + 1
            
            for c in t:
                if c in sDict and sDict.get(c,0) > 0:
                    sDict[c] -= 1
                else:
                    return False
            return True
            


def testisAnagram():
    s = "anagram" 
    t = "nagaram"
    print(Solution.isAnagramSort(Solution,s,t))
    
    s = "rat"
    t = "car"
    print(Solution.isAnagramSort(Solution,s,t))

    s = "anagram" 
    t = "nagaram"
    print(Solution.isAnagram(Solution,s,t))

    s = "rat"
    t = "car"
    print(Solution.isAnagram(Solution,s,t))


testisAnagram()
