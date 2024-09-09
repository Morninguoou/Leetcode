class Solution(object):
    def lengthOfLastWord(self, s):
        cut = s.strip()
        newS = cut[::-1]
        l = newS.find(" ")
        if l == -1 :
            return len(newS)
        else: return l