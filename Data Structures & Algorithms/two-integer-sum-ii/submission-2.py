class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers)-1

        while l <=r:
            res = numbers[l]+numbers[r]
            if res == target:
                return [l+1,r+1]
            if res < target:
                l +=1
            else:
                r -=1

      




















































        """
        for i in range(len(numbers)):
            for j in range(i + 1,len(numbers)):
                if numbers[i]+numbers[j] == target:
                    return [i+1,j+1]
        """
        # nums = []
        # for num in numbers:
        #     nums.append(num)
        

        # for i, value in enumerate(numbers):
        #     complement = target - value
        #     index = nums.index(complement)
        #     if complement in nums and i < index:
        #         return [i+1, index + 1]









                