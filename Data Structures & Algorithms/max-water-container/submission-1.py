class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        maxx = 0
        for i in range(len(heights)):
            j= i + 1
            while j < len(heights):
                area = (j-i) * min(heights[i],heights[j])
                maxx = max(maxx,area)
                j +=1
        return maxx
        """

        l,r = 0, len(heights)-1
        maxx = 0

        while l < r:
            area = (r-l) * min(heights[l],heights[r])
            maxx = max(maxx,area)
            if heights[l] > heights[r]:
                r -=1
            else:
                l +=1
        return maxx
