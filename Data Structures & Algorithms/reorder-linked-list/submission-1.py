# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        i = head
        j = head
        first = []
        while j.next != None:
            if j.next.next == None:
                j = j.next
            else:
                j = j.next.next
            first.append(i)
            i = i.next
        
        last = [i]
        while i.next != None:
            i = i.next
            last.append(i)

        a = None
        b = None
        while first or last:
            if first:
                a = first.pop(0)
                if b:
                    b.next = a
                b = last.pop()
                a.next = b
            else:
                a = b
                b = last.pop()
                if a:
                    a.next = b
                else:
                    a = b
            
        b.next = None

        head = a

        
        