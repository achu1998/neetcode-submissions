class Solution:

    def isPal(self, i, j, s):
        cnt = 0
        while i >= 0 and j < len(s) and s[i] == s[j]:
            cnt += 1
            i -=1
            j += 1
        return cnt    


    def countSubstrings(self, s: str) -> int:
        cnt = 0
        for i in range(len(s)):
            #odd
            cnt += self.isPal(i, i, s)
            #even
            cnt += self.isPal(i, i+1, s)
        return cnt    