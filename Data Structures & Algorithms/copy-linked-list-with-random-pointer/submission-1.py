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
            if newHead.random:
                newHead.random = oldToNew[newHead.random]
            newHead = newHead.next

        return begN

        

        
