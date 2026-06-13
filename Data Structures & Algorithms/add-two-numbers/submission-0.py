# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        l_res = None
        res_head = l_res
        while l1 or l2:
            if l1:
                a = l1.val
                l1 = l1.next
            else:
                a = 0
            if l2:
                b = l2.val
                l2 = l2.next
            else:
                b = 0
            t_sum = carry+a+b
            v_res = t_sum % 10
            carry = t_sum // 10
            n_res = ListNode(val=v_res, next= None)
            if not l_res:
                l_res = n_res
                res_head = l_res
            else:
                l_res.next = n_res
                l_res = l_res.next
        if carry:
            n_res = ListNode(val=carry, next=None)
            l_res.next = n_res
            l_res = l_res.next
        
        return res_head

            
        