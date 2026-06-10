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
        if not head:
            return None
        
        new_current = Node(head.val, None, None)
        new = new_current

        current = head
        node_dict = {current: 0}
        new_node_dict = {0: new_current} 
        c = 1
        while current.next: 
            current = current.next
            node_dict[current] = c
            new_current.next = Node(current.val, None, None)
            new_node_dict[c] = new_current.next
            new_current = new_current.next
            c += 1

        current = head
        new_current = new
        while current:
            if not current.random:
                new_current.random = None
            else:
                rnd_idx = node_dict[current.random]
                rdn_node = new_node_dict[rnd_idx]
                new_current.random = rdn_node

            current = current.next
            new_current = new_current.next
        
        return new

        