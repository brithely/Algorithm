"""
2023.07.16
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
Easy
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_length = len(needle)
        first_needle = needle[0]
        for i, stack in enumerate(haystack):
            if i + needle_length > len(haystack):
                return -1
            if stack == first_needle:
                if haystack[i:i+needle_length] == needle:
                    return i
        return -1
        