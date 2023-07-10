"""
2023.07.10
https://leetcode.com/problems/minimum-depth-of-binary-tree/
Easy
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, depth, node, depth_list):
        if not node.left and not node.right:
            return depth_list.append(depth)
        depth += 1
        if node.left:
            self.dfs(depth, node.left, depth_list)
        if node.right:
            self.dfs(depth, node.right, depth_list)

    def minDepth(self, root: Optional[TreeNode]) -> int:
        depth_list = []
        if not root:
            return 0
        self.dfs(1, root, depth_list)
        return min(depth_list)