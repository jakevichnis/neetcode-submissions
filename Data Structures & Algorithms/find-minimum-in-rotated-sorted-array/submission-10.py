class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        results = nums[0]
        while left <= right:
            if nums[left] < nums[right]:
                results = min(results, nums[left])
                break
                
            mid = (left + right) // 2
            results = min(results, nums[mid])
            if nums[mid] >= nums[left]: # had to switch equal signs here from nums[mid] < nums[left], i possibly if i sat with this long enough may have gotten it eventually
                left = mid + 1
            else:
                right = mid - 1 
        return results
            
