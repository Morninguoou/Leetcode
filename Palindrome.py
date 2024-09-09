class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 :
            return False
        original = str(x)
        # reverse string
        rev = original[::-1] 
        if (original == rev):
            return True
        else: False
