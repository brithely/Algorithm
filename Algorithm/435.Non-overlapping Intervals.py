"""
2023.07.19
https://leetcode.com/problems/non-overlapping-intervals/
Medium
"""


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x:x[1])
        pre_i = -math.inf
        count = 0
        for i in intervals:
            if i[0] >= pre_i:
                pre_i = i[1]
            else:
                count += 1
        return count