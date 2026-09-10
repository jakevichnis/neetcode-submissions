class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        nums1 = nums[:-1]
        nums2 = nums[1:]
        dp1 = [0] * len(nums1) # the DP table
        dp1[0] = nums1[0]     # base case
        dp1[1] = max(nums1[0], nums1[1])  # base case

        for i in range(2, len(nums1)):
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums1[i])     # recurrence

        take_1st = dp1[-1]


        # now we take the second (and are able to take the last)
        dp2 = [0] * len(nums2) # the DP table
        dp2[0] = nums2[0]     # base case
        dp2[1] = max(nums2[0], nums2[1])  # base case

        for i in range(2, len(nums2)):
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums2[i])     # recurrence


        take_2nd = dp2[-1]
        return max(take_1st, take_2nd)
