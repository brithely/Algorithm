"""
2023.07.29
https://leetcode.com/problems/soup-servings/
Medium
"""

class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4450:
            return 1
        @cache
        def serve(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            elif a <= 0:
                return 1
            elif b <= 0:
                return 0
            
            return 0.25 * (serve(a-100, b) + serve(a-75, b-25) + serve(a-50, b-50) + serve(a-25, b-75))
        return serve(n, n)