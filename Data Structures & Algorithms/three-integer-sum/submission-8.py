class Solution:
    def threeSum(self, nums):
        nums.sort()
        results = []
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            if nums[i] > 0:
                break
            elif nums[i] == nums[i-1] and i > 0:
                continue
            while left < right:
                current = nums[i] + nums[left] + nums[right]
                if current == 0:
                    results.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif current < 0:
                    left += 1
                else:
                    right -= 1
        return results