# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
    # if both p and q are SMALLER than root:
            if (p.val < root.val) and (q.val < root.val):
        # go left
                root = root.left
    # if both p and q are LARGER than root:
            elif (p.val > root.val and q.val > root.val):
        # go right
                root = root.right
    # otherwise:
            else:
        # root is the lowest common ancestor
                return root