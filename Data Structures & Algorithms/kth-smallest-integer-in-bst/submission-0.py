# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0
        node = root
        if counter == k:
            return node.val
        
        def helper(node):
            nonlocal counter
            if node is None:
                return
            left_result = helper(node.left)
            if left_result:
                return left_result
            counter += 1
            if counter == k:
                return node.val
            right_result = helper(node.right) 
            if right_result:
                return right_result
        return helper(root)