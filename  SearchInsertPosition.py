class Solution(object):
    def searchInsert(self, nums, target):
        ans = 0
        if target > nums[len(nums)-1]:
            ans = len(nums)
        for i in range(len(nums)):
            if target <= nums[i] and target > nums[i-1]:
                ans = i
        return ans