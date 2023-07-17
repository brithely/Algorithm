"""
2023.07.17
https://leetcode.com/problems/add-two-numbers-ii/
Medium
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_stack = []
        l2_stack = []
        def next_node(l1_node, l2_node):
            l1_node_next, l2_node_next = None, None
            if l1_node is None and l2_node is None:
                return 1
            if l1_node:
                l1_stack.append(l1_node.val)
                l1_node_next = l1_node.next
            if l2_node:
                l2_stack.append(l2_node.val)
                l2_node_next = l2_node.next
            next_node(l1_node_next, l2_node_next)
        next_node(l1, l2)
        up_to = 0
        next_node_val = None
        for a, b in zip_longest(reversed(l1_stack), reversed(l2_stack)):
            if a is None:
                a = 0
            if b is None:
                b = 0
            val = (a + b) + up_to
            if val >= 10:
                val = val - 10
                up_to = 1
            else:
                up_to = 0
            next_node_val = ListNode(val, next_node_val)
        if up_to > 0:
            next_node_val = ListNode(up_to, next_node_val)
        return next_node_val