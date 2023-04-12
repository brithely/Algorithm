"""
2023.04.12
https://leetcode.com/problems/simplify-path/
Medium
"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        slash_split = path.split("/")
        answer = []
        for s in slash_split:
            if s == "":
                continue
            if s == ".":
                continue
            if s == "..":
                if answer:
                    answer.pop()
                continue
            answer.append(f"{s}")
        return f"/{'/'.join(answer)}"
