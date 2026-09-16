# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        headOne = list1
        headTwo = list2

        if not headOne:
            if headTwo:
                return headTwo
            else:
                return headOne
        if not headTwo:
            return headOne

        final = None

        if headOne.val <= headTwo.val:
            final = headOne
            headOne = headOne.next
            final.next = None
        else:
            final = headTwo
            headTwo = headTwo.next
            final.next = None
        
        finalHead = final

        while headOne and headTwo:
            if headOne.val <= headTwo.val:
                final.next = headOne
                headOne = headOne.next
                final = final.next
                #final.next = None
            else:
                final.next = headTwo
                headTwo = headTwo.next
                final = final.next
                #final.next = None

        if headOne:
            final.next = headOne
        elif headTwo:
            final.next = headTwo

        return finalHead
        

        