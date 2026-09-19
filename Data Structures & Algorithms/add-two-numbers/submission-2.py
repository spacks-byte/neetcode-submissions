# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        newHead = ListNode()
        beg = newHead
        while l1 and l2:
            total = l1.val + l2.val + carry
            newHead.next = ListNode(total % 10)
            carry = total // 10
            newHead = newHead.next
            l1 = l1.next
            l2 = l2.next

        # add carry to the next one
        
        if l1:
            while l1 and carry:
                total = l1.val + carry
                newHead.next = ListNode(total % 10)
                carry = total // 10
                newHead = newHead.next
                l1 = l1.next
            if carry:
                newHead.next = ListNode(carry)
            else:
                newHead.next = l1
        elif l2:
            while l2 and carry:
                total = l2.val + carry
                newHead.next = ListNode(total % 10)
                carry = total // 10
                newHead = newHead.next
                l2 = l2.next
            if carry:
                newHead.next = ListNode(carry)
            else:
                newHead.next = l2
        elif carry:
            newHead.next = ListNode(carry)

        return beg.next


        