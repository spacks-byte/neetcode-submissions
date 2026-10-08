# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kth = 0

        def helper(node, offset) -> int:
            nonlocal kth
            if not node:
                return 0
            left = 0
            right = 0

            if node.left:
                left = helper(node.left, 0)

            val = left + offset
            if val == k-1:
                kth = node.val

            if node.right:
                right = helper(node.right, left+1+offset)
            return 1 + right + left
        
        helper(root, 0)
        return kth    