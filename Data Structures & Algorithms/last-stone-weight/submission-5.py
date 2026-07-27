class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        temp = [-num for num in stones]
        heapq.heapify(temp)
        if len(temp) == 1:
            return -temp[0]
        while len(temp) > 1:
            x = -heapq.heappop(temp)
            y = -heapq.heappop(temp)

            if y != x:
                heapq.heappush(temp,-(x - y))
            
        if len(temp) > 0:
            return -temp[0]
        return 0 

        

        