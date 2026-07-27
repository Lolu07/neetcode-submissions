class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        length of longest consecutive numbers in array
        array is not sorted
        a number is consecutive if its +1 value or -1 value exists in array
        no duplicates allowed
        lookup in set is O(1)
        convert list to a set for lookup and removal of duplicates
        the start of a sequence exists if the -1 of that number is not in the set
        create a max_no variable to keep track of the longest consecutive sequence
        to keep track of a consecutive sequence use a while loop inside the for loop iteration 
        to check for if the +1 of a value exists in the set
        """

        nums_set = set(nums)
        max_count = 0

        for num in nums_set:
            cur_count = 1
            if num -1 not in nums_set:
                while num +1 in nums_set:
                    cur_count +=1
                    num +=1
            max_count = max(max_count, cur_count)
        return max_count
