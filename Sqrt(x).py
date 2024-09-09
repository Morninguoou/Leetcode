class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        for i in range(x):
            if i == 1 or i == 0:
                continue
            elif x % i == 0 :
                check = x / i
                if check / i == 1:
                    return i