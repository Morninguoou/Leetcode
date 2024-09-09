class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        total = 0
        isMinus = False
        if x < 0:
            x *= -1
            isMinus = True
        while x != 0:
            total *= 10
            num = x % 10
            total += num
            x = x // 10
        if isMinus:
            total *= -1
        if total < (-2)**31 or total > (2**31) - 1: return 0
        else: return total