class Solution:
    #O(n^2)
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):                
                if nums[i] + nums[j] == target and i != j:
                    return i, j
            
def testTwoSum():
    nums = [2,7,11,15]
    target = 9
    print(Solution.twoSum(Solution, nums, target))
    
    nums = [3,2,4] 
    target = 6
    print(Solution.twoSum(Solution, nums, target))

    nums = [3,3] 
    target = 6
    print(Solution.twoSum(Solution, nums, target))


testTwoSum()