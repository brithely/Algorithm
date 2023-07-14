"""
2023.07.14
https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/
Medium
"""

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        longest_dict = defaultdict(int)
        max_length = 0
        for i in arr:
            longest_dict[i] = longest_dict[i - difference] + 1
            max_length = max(longest_dict[i], max_length)
        return max_length
