class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * (n+1)
        if n == 1: return nums[0]

        def dfs(i, n, dp, nums):
            if i >= n-1: return 0
            if dp[i] != -1:
                return dp[i]

            take = nums[i] + dfs(i+2, n, dp, nums)
            notake = dfs(i+1, n, dp, nums)
            dp[i] = max(take, notake)
            return dp[i]    

        return max(dfs(0, n, dp[:], nums[:-1]) , dfs(0, n, dp[:], nums[1:]))