"""
2023.07.28
https://leetcode.com/problems/predict-the-winner/
Medium
"""

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        p1 = 0
        p2 = 0
        def choose(p1, p2, cp, nums):
            if not nums:
                if p1 >= p2:
                    return True
                return False
            if cp == 1:
                left = choose(p1+nums[0], p2, 2, nums[1:])
                right = choose(p1+nums[-1], p2, 2, nums[:-1])
                return left or right
            else:
                left = choose(p1, p2+nums[0], 1, nums[1:])
                right = choose(p1, p2+nums[-1], 1, nums[:-1])
                return left and right

        return choose(p1, p2, 1, nums)