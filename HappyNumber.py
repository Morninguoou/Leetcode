class Solution(object):
    def isHappy(self, n):
        def isFinish(n, seen):
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
            total = 0
            while n != 0:
                cur = n % 10
                total += cur * cur
                n = n // 10
            return isFinish(total, seen)
        
        return isFinish(n, set())