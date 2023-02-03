"""
2023.02.04
https://leetcode.com/problems/add-two-numbers/
Easy
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def list_from_linked_list(self, n, n2, n3, upper):
        new_value = 0
        if upper:
            new_value = upper
            upper = 0
        if n and n2:
            new_value += n.val + n2.val
            if new_value >= 10:
                new_value = new_value - 10
                upper = 1
        elif n:
            new_value += n.val
            if new_value >= 10:
                new_value = new_value - 10
                upper = 1
        elif n2:
            new_value += n2.val
            if new_value >= 10:
                new_value = new_value - 10
                upper = 1
        new_node = ListNode()
        n_next = None
        n2_next = None
        n3.val = new_value

        if (n and n.next) or (n2 and n2.next) or upper:
            if n:
                n_next = n.next
            if n2:
                n2_next = n2.next
            n3.next = new_node
            self.list_from_linked_list(n_next, n2_next, new_node, upper)


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l = ListNode()
        self.list_from_linked_list(l1, l2, l, 0)
        return l