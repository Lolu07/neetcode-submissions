class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        the product of all other numbers in the array except the self or current element
        no number is unique and array is not sorted 
        0 can be part of the array of numbers and anything multiplied by 0 is = 0
        we can multiply all elements in the array and have a total product
        since multiplication and division are inverse 
        we can divide each element by the total product to get the total 
        gotten from multiplying all other elements except the divisor
        but we also have to account for 0 and we can do that by keeping track
        of the zero count in the array 
        if the zero count is greater than 1 we know everything will be 0 because 
        no matter the element we are on there is always going to be a 0 that will multiply everything and give 0
        but for the case where the zero count is 1 we know the output array will be all 0 except
        for when the index is on the position of the 0 element,
        in that case we will have an actual value since all other elements at that point are not oif the value 0
        """

        prod = 1
        zero_count = 0
        res = [0] * len(nums)

        for num in nums:
            if num != 0:
                prod *= num
            else:
                zero_count +=1
                continue
        
        if zero_count > 1:
            return [0] * len(nums)
        
        for i,value in enumerate(nums):
            if zero_count:
                if value == 0:
                    res[i] = prod
                else:
                    res[i] = 0
            else:
                res[i] = prod//value
        return res

        

        


        