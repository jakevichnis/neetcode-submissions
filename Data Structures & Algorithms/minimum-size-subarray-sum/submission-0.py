class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current = 0
        output = float("inf")
        for right in range(len(nums)):
            current += nums[right]
            while current >= target:
                output = min(right - left + 1, output)
                current -= nums[left]
                left += 1
        return 0 if output == float("inf") else output
                
