"""
2023.07.08
https://leetcode.com/problems/search-insert-position/
Easy
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        for _ in range(len(nums)):
            pivot = int((left + right) / 2)
            if (right - left) < 2:
                if nums[pivot] >= target:
                    return left
                else:
                    return right
            elif nums[pivot] > target:
                right = pivot
            elif nums[pivot] < target:
                left = pivot
            else:
                return pivot