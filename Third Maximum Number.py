class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
        for n in nums:
            if n not in result:
                result.append(n)
        result.sort()
        if len(result) < 3 :
            return result[-1]
        else: return result[-3]