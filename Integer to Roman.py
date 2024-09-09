class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        IntToRoman = {
            1 : "I",
            4 : "IV",
            5 : "V",
            9: "IX",
            10 : "X",
            40 : "XL",
            50 : "L",
            90 : "XC",
            100 : "C",
            400 : "CD",
            500 : "D",
            900 : "CM",
            1000 : "M" 
        }
        mod = 10
        mul = 1
        resultRe = []
        while num != 0:
            temp = num % mod
            if temp in IntToRoman:
                resultRe.append(IntToRoman[temp])
            elif temp >= 5*mul:
                temp -= 5*mul
                for i in range(temp//mul):
                    resultRe.append(IntToRoman[mul])
                resultRe.append(IntToRoman[5*mul])
                temp += 5*mul
            else:
                for i in range(temp//mul):
                    resultRe.append(IntToRoman[mul])
            mod *= 10
            mul *= 10
            num -= temp
        result = resultRe[::-1]
        ans = "".join(result)
        return ans