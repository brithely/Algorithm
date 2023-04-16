"""
2023.02.13
https://leetcode.com/problems/longest-common-prefix/
Easy
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_length = max(map(len, strs))
        result = ""
        for i in range(max_length):
            for j, s in enumerate(strs):
                try:
                    if j == 0:
                        temp = s[i]
                    if temp != s[i]:
                        temp = ""
                        break
                except IndexError:
                    temp = ""
                    break
            if temp == "":
                break
            else:
                result += temp
        return result
