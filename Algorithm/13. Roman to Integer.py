"""
2022.12.07
https://leetcode.com/problems/roman-to-integer/
Easy
"""


class Solution:
    def roman_to_arabic(self, roman: str):
        roman_to_arbic_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        return roman_to_arbic_map.get(roman)

    def romanToInt(self, s: str) -> int:
        s_length = len(s)
        number_list = []
        current = 0
        for i in range(s_length):
            if current >= s_length:
                break
            roman_num = s[current]
            slicing_num = 0
            last = s_length == current + 1

            if roman_num in ["I", "X", "C"]:
                if not last:
                    next_roman_num = s[current + 1]
                    if (
                        (roman_num == "I" and next_roman_num in ["V", "X"])
                        or (roman_num == "X" and next_roman_num in ["L", "C"])
                        or (roman_num == "C" and next_roman_num in ["D", "M"])
                    ):
                        slicing_num = 2
            if slicing_num:
                number_list.append(
                    self.roman_to_arabic(s[current : current + slicing_num])
                )
                current += 2
            else:
                number_list.append(self.roman_to_arabic(s[current]))
                current += 1
        return sum(number_list)
