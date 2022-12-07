"""
2022.11.16
https://leetcode.com/problems/min-cost-climbing-stairs/
Easy
Dynamic Programming
"""


from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost[-1], cost[-2])
        if len(cost) == 1:
            return cost[0]
        for index, cost_element in enumerate(cost[2:], 2):
            cost[index] = cost_element + min(cost[index - 1], cost[index - 2])
        return min(cost[-1], cost[-2])


print(Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
