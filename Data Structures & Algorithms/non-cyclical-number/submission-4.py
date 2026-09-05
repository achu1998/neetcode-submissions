class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            if n == 1: return True
            if n in seen: return False
            seen.add(n)
            temp = 0
            num = n
            while num:
                s = num % 10
                temp += s ** 2
                num = num // 10
            n = temp
                
