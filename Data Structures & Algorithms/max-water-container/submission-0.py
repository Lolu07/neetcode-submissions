class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxx = 0
        for i in range(len(heights)):
            j= i + 1
            while j < len(heights):
                area = (j-i) * min(heights[i],heights[j])
                maxx = max(maxx,area)
                j +=1
        return maxx
