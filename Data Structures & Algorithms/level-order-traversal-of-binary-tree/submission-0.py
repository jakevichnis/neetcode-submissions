# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if root is None:
            return []
        # start a queue as a deque starting w/ root level
        queue = deque([root])
        result = []
        while queue:
            current_level = []
            length = len(queue)
            # process whatever nodes on level...
            for _ in range(length):
                # removes front of the queue
                node = queue.popleft()
                current_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)
        return result