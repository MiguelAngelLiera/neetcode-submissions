# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ant = None
        while head is not None:
            new = head.next
            head.next = ant
            ant = head
            head = new

        return ant  
        
        