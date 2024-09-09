class Solution(object):
    def romanToInt(self, s):
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        pre_value = roman_to_int[s[0]]
        newS = s[1:]
        total += pre_value
        for char in newS:
            cur_value = roman_to_int[char]
            if pre_value >= cur_value:
                total += cur_value
            else: total = total + (cur_value - pre_value*2)
            pre_value = cur_value
        return total