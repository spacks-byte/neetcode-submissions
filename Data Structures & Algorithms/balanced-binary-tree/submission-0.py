# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    UNBALANCED = False
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        global UNBALANCED
        self.DFS(root)
        return not self.UNBALANCED

    def DFS(self, root: Optional[TreeNode]) -> bool:
        global UNBALANCED
        if self.UNBALANCED:
            return 0
        
        if not root:
            return 0

        left = self.DFS(root.left)
        right = self.DFS(root.right)

        if abs(left-right) > 1:
            self.UNBALANCED = True

        return left +1 if left > right else right +1
    