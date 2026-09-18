# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        begR = slow.next
        slow.next = None
        
        prev = None
        while begR != None:
            temp = begR.next
            begR.next = prev
            prev = begR
            begR = temp          

        first = head
        second = prev

        flip = True
        while second:
            tempOne = first.next
            tempTwo = second.next

            if flip:
                first.next = second
                first.next.next = tempOne
                second = tempTwo
            
            flip = not flip
            first = first.next
        




        