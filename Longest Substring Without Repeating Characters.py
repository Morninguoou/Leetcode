class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if s == "":
            return 0
        if s == " " or len(s) == 1:
            return 1
        n = 0
        length = []
        mem = []
        while n < len(s):
            if s[n] not in mem:
                mem.append(s[n])
            elif s[n] in mem:
                length.append(len(mem))
                while mem[0] != s[n]:
                    mem.pop(0)
                mem.pop(0)
                mem.append(s[n])
            n+=1
        length.append(len(mem))
        if len(length) == 0:
            return len(s)
        else: return max(length)