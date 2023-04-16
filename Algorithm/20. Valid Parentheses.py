"""
2023.04.17
https://leetcode.com/problems/valid-parentheses/
Easy
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        result = True
        for i, bracket in enumerate(s):
            if bracket in ["(", "{",  "["]:
                stack.append(bracket)
            if bracket in [")", "}", "]"]:
                if len(stack) <= 0:
                    return False
                temp = stack.pop()
                if bracket == ")" and not temp == "(":
                    result = False
                    break
                if  bracket == "}" and not temp == "{":
                    result = False
                    break
                if  bracket == "]" and not temp == "[":
                    result = False
                    break
        if len(stack) > 0:
            result = False
        return result
            