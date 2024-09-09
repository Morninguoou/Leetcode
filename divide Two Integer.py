class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        ans = dividend // divisor
        if negative:
            ans = -ans

        return max(min(ans, 2147483647), -2147483648)