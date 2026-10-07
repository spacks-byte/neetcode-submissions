# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0

        def dfs(node, max) -> int:
            left, right, cur = 0, 0, 0
            if node.val >= max:
                cur = 1
                max = node.val
            if node.left:
                left = dfs(node.left, max)
            if node.right:
                right = dfs(node.right, max)
            return cur + left + right
        
        return dfs(root, root.val)
        