# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        import math
    
        if not root:
            return False

        def helper(node, lt, gt) -> int:
            val = node.val
            if not (val > gt and val < lt):
                return False
            if node.left:
                if not (val > node.left.val):
                    return False
                left = helper(node.left, val, gt)
                if not left:
                    return left
            if node.right:
                if not (val < node.right.val):
                    return False
                right = helper(node.right, lt, val)
                if not right:
                    return right
            return True
        
        return helper(root, math.inf, -math.inf)
            