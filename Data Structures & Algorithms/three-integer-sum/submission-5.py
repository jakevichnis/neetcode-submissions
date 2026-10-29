class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums)):
            if nums[0] > 0:
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                current = nums[i] + nums[left] + nums[right]
                if current == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left = left + 1
                    right = right - 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif current < 0:
                    left += 1
                else:
                    right -= 1
        return result