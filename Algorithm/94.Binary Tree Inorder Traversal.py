"""
2023.01.30
https://leetcode.com/problems/binary-tree-inorder-traversal/
Easy
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder_binary_tree(self, node, inorder_list):
        if not node:
            return inorder_list
        if node.left:
            self.inorder_binary_tree(node.left, inorder_list)
        inorder_list.append(node.val)
        if node.right:
            self.inorder_binary_tree(node.right, inorder_list)
        return inorder_list

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorder_binary_tree(root, [])