class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freqDict = {}
        resList = []

        for num in nums:
            if num in freqDict:
                freqDict[num] += 1
            else:
                freqDict[num] = 1
        
        for i in range(k):
            max_key = max(freqDict, key=freqDict.get)
            resList.append(max_key)
            del freqDict[max_key]
            
        return resList
            
def testFreq():
    nums = [1,1,1,2,2,3]
    k = 2
    print(Solution.topKFrequent(Solution, nums, k))
    #Output: [1,2]

    nums = [1]
    k = 1
    print(Solution.topKFrequent(Solution, nums, k))
    #Output: [1]

    nums = [1,2]
    k = 2
    print(Solution.topKFrequent(Solution, nums, k))
    #Output: [1,2]


testFreq()