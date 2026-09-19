# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    DIAMETER = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global DIAMETER
        self.DFS(root)
        return self.DIAMETER

    def DFS(self, root: Optional[TreeNode]) -> int:
        global DIAMETER
        if not root:
            return 0

        left = self.DFS(root.left)
        right = self.DFS(root.right)

        if left + right > self.DIAMETER:
            self.DIAMETER = left+right

        return left+1 if left > right else right+1
    

        