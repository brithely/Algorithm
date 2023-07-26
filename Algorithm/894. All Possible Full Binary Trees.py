"""
2023.07.23
https://leetcode.com/problems/all-possible-full-binary-trees/
Medium
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    dp = {
        1: [TreeNode()],
        3: [TreeNode(left=TreeNode(), right=TreeNode())]
    }
    def solve(self, n):
        if n in self.dp:
            return self.dp[n]
        else:
            result = []
            for i in range(1, n - 1, 2):
                left = self.solve(i)
                self.dp[i] = left
                right = self.solve(n - i -1)
                self.dp[n- i - 1] = right
                for l_sub_tree in left:
                    for r_sub_tree in right:
                        result.append(TreeNode(left=l_sub_tree, right=r_sub_tree))
            return result 

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        return self.solve(n)