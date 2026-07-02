class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        window_max = nums[left:k]
        pos = []
        pos.append(max(window_max))
        for right in range(k, len(nums)):
            pos.append(max(nums[left+1:right+1]))
            left +=1
        return pos