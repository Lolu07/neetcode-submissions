class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #given array of int and a target value
        #return indices of i and j
        #such that nums[i]+nums[j]==target
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
                
        