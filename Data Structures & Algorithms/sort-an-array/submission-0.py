class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1: # Base case
            return nums
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid]) # Sort left half
        right = self.sortArray(nums[mid:]) # Sort right half
        # Merge sorted halves
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:]) # Add remaining
        result.extend(right[j:])
        return result