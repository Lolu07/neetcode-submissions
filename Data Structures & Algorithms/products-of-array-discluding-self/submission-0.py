class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #in an array nums return output where,
        #output[i] is the product of all other elements in array except itself
        #i can use slicicng and the math.prod method to get the output of each element
        
        output =[0] * len(nums)      
        output[0] = math.prod(nums[1:])     
        output[len(nums)-1] = math.prod(nums[len(nums)-2::-1])
        i =1

        while i < len(nums)-1:            
            output[i] = (math.prod(nums[i+1:])) * (math.prod(nums[i-1::-1]))
            i +=1
        return output

        