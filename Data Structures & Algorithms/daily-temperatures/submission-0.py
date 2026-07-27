class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []


        for i,num in enumerate(temperatures):

            while stack and stack[-1][0] < num:
                t,indx = stack.pop()
                result[indx] = i - indx
            stack.append((num,i))
        return result
        