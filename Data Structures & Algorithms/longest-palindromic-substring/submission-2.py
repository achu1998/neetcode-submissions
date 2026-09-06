class Solution:

    def isPal(self, i, j, s):
        while i >=0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return i+1, j-1    

    def longestPalindrome(self, s: str) -> str:
        long = 0
        res = ''
        for i in range(len(s)):
            # odd
            x, y = self.isPal(i, i, s)
            if y-x+1 > long:
                res  = s[x:y+1]
                long = y-x+1
            #even
            x, y = self.isPal(i, i+1, s)
            if y-x+1 > long:
                res  = s[x:y+1]
                long = y-x+1
        return res        