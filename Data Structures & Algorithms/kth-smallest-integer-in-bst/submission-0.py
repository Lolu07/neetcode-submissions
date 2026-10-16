# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        queue = deque([root])
        arr = []
        while queue:
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                arr.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        minimum = 0
        heapq.heapify(arr)
        for _ in range(k):
            minimum = heapq.heappop(arr)
        return minimum
