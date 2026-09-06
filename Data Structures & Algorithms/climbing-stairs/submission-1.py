class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n+1)
        def dfs(i, dp):
            if i == 0 or i == 1: return 1
            if i < 0: return 0
            if dp[i] != -1: return dp[i]
            one = dfs(i-1, dp)
            two = dfs(i-2, dp)
            dp[i] = one + two
            return dp[i]    
        return dfs(n, dp)