class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()

        for num in nums:
            if num in seen:
                return num
            else:
                seen.add(num)
                


                

                """
                for i in range(1,len(nums)):
            j = i
            while j -1 >= 0:
                j -=1
                if nums[i] == nums[j]:
                    return nums[i]
                """
        