class Solution(object):
    def removeDuplicateLetters(self, s):
        ans = []
        for n in s:
            if n not in ans:
                ans.append(n)
            elif n in ans:
                ans.remove(n)
                ans.append(n)
        re = "".join(ans)
        return re