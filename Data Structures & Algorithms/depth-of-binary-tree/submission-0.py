# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        if right and left:
            if right > left:
                return right + 1
            else:
                return left + 1
        elif right:
            return right + 1
        elif left:
            return left + 1
        else:
            return 1

        