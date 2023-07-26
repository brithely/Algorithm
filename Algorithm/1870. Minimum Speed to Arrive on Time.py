"""
2023.07.26
https://leetcode.com/problems/minimum-speed-to-arrive-on-time/
Medium
"""

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) - 1 >= hour:
            return -1
        
        left, right = 1, 10 ** 7
        low_speed = math.inf
        while left <= right:
            speed = int((left + right) / 2)
            
            time = sum((sum([math.ceil(i/speed) for i in dist[:-1]]), dist[-1]/speed))
            if time <= hour:
                if speed < low_speed:
                    low_speed = speed
                right = speed -1
            else:
                left = speed + 1
        return low_speed