"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # dfs and build on the way back up while keeping trackof visited neighbours
        if not node:
            return None

        created = {}

        def dfs(itself: Node):
            if created.get(itself, None):
                return created[itself]
            newNode = Node(itself.val, [])
            created[itself] = newNode
            for neighbor in itself.neighbors:
                newNode.neighbors.append(dfs(neighbor))
  
            return newNode

        return dfs(node)