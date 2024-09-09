class Solution(object):
    def isValid(self, s):
        stack = []
        for char in s:
            if char == "{" or char == "[" or char == "(":
                stack.append(char)
            elif char == "}":
                if len(stack) == 0 or stack[-1] != "{": return False
                else: stack.pop()
            elif char == ")":
                if len(stack) == 0 or stack[-1] != "(": return False
                else: stack.pop()
            elif char == "]":
                if len(stack) == 0 or stack[-1] != "[": return False
                else: stack.pop()
        if len(stack) == 0 :return True
        else: return False
            