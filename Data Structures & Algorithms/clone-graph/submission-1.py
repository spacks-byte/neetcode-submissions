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
                return
            newNode = Node(itself.val, [])
            created[itself] = newNode
            for neighbor in itself.neighbors:
                newNeighbor = created.get(neighbor, None)
                if not newNeighbor:
                    newNeighbor = dfs(neighbor)
                newNode.neighbors.append(newNeighbor)
                        
            return newNode

        return dfs(node)