"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {}
        newHead = Node(0)
        begN = newHead

        while head:
            newHead.next = Node(head.val, None, head.random)
            newHead = newHead.next
            oldToNew[head] = newHead
            head = head.next
            
        begN = begN.next
        newHead = begN

        while newHead:
            oldRandom = newHead.random
            if oldRandom:
                newHead.random = oldToNew[oldRandom]
            newHead = newHead.next

        return begN

        

        
