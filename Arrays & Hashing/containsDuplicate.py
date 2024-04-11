#Worst case runtime for this solution is:
# - O(n)
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        numsDict = {}
        for num in nums:
            if num in numsDict:  
                return True
            else:
                numsDict.update({num: '1'})
        return False

def testContainsDuplicate():
    nums = [1,2,3,1]
    print(Solution.containsDuplicate(Solution, nums))
    nums = [1,2,3,4]
    print(Solution.containsDuplicate(Solution, nums))
    nums = [1,1,1,3,3,4,3,2,4,2]
    print(Solution.containsDuplicate(Solution, nums))

testContainsDuplicate()