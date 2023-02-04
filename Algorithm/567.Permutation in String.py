"""
2023.02.05
https://leetcode.com/problems/permutation-in-string/
Medium
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        permutation_list = []
        sorted_s1 = sorted(s1)
        len_s1 = len(s1)
        len_s2 = len(s2)
        for i in range((len_s2-len_s1)+1):
            sorted_s2 = sorted(s2[i:i+len_s1])
            if sorted_s1 == sorted_s2:
                return True
        return False