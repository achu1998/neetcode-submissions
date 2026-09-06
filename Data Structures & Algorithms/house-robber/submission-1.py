class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * (n+1)
        def dfs(ind, n , dp, nums):
            if ind >= n: return 0
            if dp[ind] != -1: return dp[ind]
            take = nums[ind] + dfs(ind+2, n, dp, nums)
            notake = dfs(ind+1, n, dp, nums)
            dp[ind] =  max(take, notake)
            return dp[ind]
        return dfs(0, n, dp, nums)