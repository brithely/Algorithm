"""
2023.07.11
https://leetcode.com/problems/valid-anagram/
Easy
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        if sorted_s == sorted_t:
            return True
        return False