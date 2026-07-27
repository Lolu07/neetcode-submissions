class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = set(nums)
        longest = 0
        for num in res:
            length = 1
            while num - 1 not in res:
                if (num + length) in res:
                    length +=1
                else:
                    break
            longest = max(longest,length)
        return longest
               
                  
        