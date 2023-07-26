"""
2023.07.22
https://leetcode.com/problems/knight-probability-in-chessboard/
Medium
"""


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        @cache
        def jump(r, c, step):
            if step == 0:
                return 1
            
            result = 0
            for r_i, c_i in knight_moves:
                if 0 <= r + r_i <= n-1 and 0 <= c + c_i <= n-1:
                    result += jump(r + r_i, c + c_i, step-1)
            return result
        knight_moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        probability = jump(row, column, k)
        return probability/8**k