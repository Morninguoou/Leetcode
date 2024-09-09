class Solution(object):
    def findComplement(self, num):
        if num == 1:
            return 0
        elif num == 0:
            return 1
        binary = []
        while num != 1:
            temp = num % 2
            binary.append(temp)
            num -= temp
            num = int(num / 2)
        binary.append(1)
        binary = binary[::-1]
        binary_re = []
        for n in binary:
            if n == 1:
                binary_re.append(0)
            elif n == 0:
                binary_re.append(1)
        binary_re = binary_re[::-1]
        total = 0
        mul = 1
        for b in binary_re:
            total += b*mul
            mul *= 2
        return total