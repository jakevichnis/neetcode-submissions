class Solution:
    def trap(self, height: List[int]) -> int:
        # pointers
        left = 0
        right = len(height) - 1
        # max length barriers
        leftMax = height[left]
        rightMax = height[right]
        # result/main output
        output = 0
        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                output += (leftMax - height[left])
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                output += (rightMax - height[right])
        return output
