class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix) * len(matrix[0])
        l = 0
        r = n -1

        while l <= r:
            mid = (l + r)//2
            mid_value = matrix[mid//len(matrix[0])][mid%len(matrix[0])]
            if mid_value == target:
                return True
            if mid_value > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
            

        