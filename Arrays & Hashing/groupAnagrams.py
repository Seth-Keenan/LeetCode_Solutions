class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anaDict = {}
        retList = []

        for s in strs:
            anaDict[s] = ''.join(sorted(s))
        
        for s in anaDict:
            

        



def testGroupAnagrams():
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(Solution.groupAnagrams(Solution, strs))
    #Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

    strs = [""]
    print(Solution.groupAnagrams(Solution, strs))
    #Output: [[""]]

    strs = ["a"]
    print(Solution.groupAnagrams(Solution, strs))
    #Output: [["a"]]

testGroupAnagrams()