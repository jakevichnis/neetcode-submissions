# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
            # recursive helper: check a node within its valid lowwer/upper bounds
        def validate(node, lower, upper):
            
            # if we've reached the end of a path:
            if node is None:
            # this path is valid
                return True
            # if this node violates either bound:
            if (node.val >= upper) or (node.val <= lower):
            # the tree is invalid
                return False
            # recursively check the left subtree
            # right side gets a new lower bound
            return validate(node.left, lower, node.val) and validate(node.right, node.val, upper)
        # start at root with no lower or upper restriction
        return validate(root, float('-inf'), float('inf'))