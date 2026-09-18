# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        beginning = head
        slow = head

        counter = 0
        while counter < n and head:
            head = head.next
            counter += 1

        prev = None
        while head:
            head = head.next
            prev = slow
            slow = slow.next
        
        if slow == beginning:
            return slow.next
        else:
            prev.next = slow.next

        return beginning