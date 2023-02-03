"""
2023.02.01
https://leetcode.com/problems/two-sum/
Easy
"""

class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i, num in enumerate(nums):
    #         for j, nested_num in enumerate(nums[i+1:]):
    #             if num + nested_num == target:
    #                 return [i, i+j+1]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sub_nums = {}
        for i, num in enumerate(nums):
            divide_index = sub_nums.get(num)
            if divide_index is not None and divide_index != i:
                return [sub_nums.get(num), i]
            sub_nums[target - num] = i