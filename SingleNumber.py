class Solution(object):
    def singleNumber(self, nums):
        ans = []
        mem = []
        for n in nums:
            if n not in ans and n not in mem:
                ans.append(n)
                mem.append(n)
            elif n in ans:
                ans.remove(n)
        return ans