"""
2023.02.06
https://leetcode.com/problems/verifying-an-alien-dictionary/
Easy
"""
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_set = {character: i for i, character in enumerate(list(order))}
        order_set.update({None: -1})
        max_length = max(map(len, words))

        index = 0
        check_list = [None for _ in range(len(words))]
        for i in range(max_length):
            order_check = -100
            for i in range(len(words)):
                if all(check_list):
                    return True
                try:
                    word = words[i][index]
                except IndexError:
                    word = None
                if check_list[i]:
                    order_check = order_set.get(word)
                    continue
                if order_set.get(word) > order_check:
                    check_list[i] = True
                elif order_set.get(word) == order_check:
                    check_list[i] = None
                elif order_set.get(word) < order_check:
                    return False
                order_check = order_set.get(word)
            index += 1
        return True