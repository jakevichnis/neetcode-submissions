class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for n in range(len(nums)):
            for i in range(n):
                if nums[i] < nums[n]:
                    dp[n] = max(dp[n], dp[i] + 1)
        return max(dp)