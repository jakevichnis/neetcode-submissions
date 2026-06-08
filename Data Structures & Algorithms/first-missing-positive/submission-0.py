class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Step 1: In-place Hashing (Cyclic Sort)
        for i in range(n):
            # Keep swapping until the element is in its correct spot
            # or it is out of the valid range [1, n], 
            # or it is a duplicate of the element already at the target index.
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with the element at its target index
                target_idx = nums[i] - 1
                nums[i], nums[target_idx] = nums[target_idx], nums[i]
        
        # Step 2: Scan for the first discrepancy
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # Step 3: If 1 through n are all present, the answer is n + 1
        return n + 1
