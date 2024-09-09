class Solution(object):
    def maximumGap(self, nums):
        if len(nums) == 1:
            return 0
        nums.sort()
        maxG = abs(nums[0]-nums[1])
        cur = nums[1]
        for i in range(2,len(nums)):
            cur_G = abs(cur - nums[i])
            maxG = max(maxG,cur_G)
            cur = nums[i]
        return maxG