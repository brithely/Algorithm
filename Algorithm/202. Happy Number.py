"""
2023.07.09
https://leetcode.com/problems/happy-number/
Easy
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        loop_check_list = []
        while True:
            sum_n = sum([int(i) ** 2 for i in str(n)])
            if sum_n in loop_check_list:
                return False 
            if sum_n == 1:
                return True
            else:
                loop_check_list.append(sum_n)
                n = sum_n
