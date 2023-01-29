"""
2023.01.29
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Medium
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = []
        max_len = 0
        for i, p in enumerate(s):
            if p in substring:
                substring = substring[substring.index(p)+1:]
            substring.append(p)
            if len(substring) > max_len:
                max_len = len(substring)
        return max_len
