class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for index, anchor in enumerate(nums):
            if anchor > 0:
                break
            if index > 0 and anchor == nums[index - 1]:
                continue
            # two pointers section
            left, right = index + 1, len(nums) - 1
            while left < right:
                threesum = anchor + nums[left] + nums[right]
                if threesum > 0:
                    right -= 1
                elif threesum < 0:
                    left += 1
                else:
                    output.append([anchor, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return output