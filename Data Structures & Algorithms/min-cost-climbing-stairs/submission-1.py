class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * (n+1)

        def dfs(ind, n, dp, cost):
            if ind >= n: return 0
            if dp[ind] != -1: return dp[ind]
            one = cost[ind] + dfs(ind+1, n, dp, cost)
            two = cost[ind] + dfs(ind+2, n, dp, cost)
            dp[ind] = min(one, two)
            return dp[ind]

        return min(dfs(0, n, dp, cost), dfs(1, n, dp, cost))