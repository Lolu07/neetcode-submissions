class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]* len(temperatures)
        
        for index, temp in enumerate(temperatures):
            if stack:
                while stack and temp > stack[-1][0]:
                    num,i = stack.pop()
                    result[i] = index - i
            stack.append((temp,index))
        return result
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
        # result = [0] * len(temperatures)
        # stack = []


        # for i,num in enumerate(temperatures):
        #     while stack and stack[-1][0] < num:
        #         t,indx = stack.pop()
        #         result[indx] = i - indx
        #     stack.append((num,i))
        # return result
        