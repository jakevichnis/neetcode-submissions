class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        # Sort the array.
        nums.sort()
        n = len(nums)
        # Iterate i from 0 to n, skipping duplicates.
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
        # For each i, iterate j from i + 1 to n, skipping duplicates.
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                # Use two pointers: left = j + 1 and right = n - 1.
                left = j + 1
                right = n - 1
            # While left < right:
                while left < right:
                    foursum = nums[i] + nums[j] + nums[left] + nums[right]
# If sum equals target, add quadruplet and move both pointers while skipping duplicates.
                    if foursum == target:
                        output.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                # If sum is less than target, increment left.
                    elif foursum < target:
                        left += 1
                # If sum is greater than target, decrement right.
                    else:
                        right -= 1
        # Return the result list.
        return output



