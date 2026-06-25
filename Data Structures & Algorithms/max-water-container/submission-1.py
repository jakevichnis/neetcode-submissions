class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_water = 0
        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            if area > max_water:
                max_water = area
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
            
        return max_water