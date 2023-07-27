"""
2023.07.27
https://leetcode.com/problems/maximum-running-time-of-n-computers/
Hard
"""

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left, right = 0, sum(batteries)//n

        while left <= right:
            time = (left + right) // 2 
            if sum([min(battery, time) for battery in batteries]) >= time * n:
                left = time + 1
            else:
                right = time - 1
        return right