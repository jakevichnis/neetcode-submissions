class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # initalize slow pointer
        left = 1
        # fast pointer runs through indices
        for right in range(1, len(nums)):
            # "if the new value is different to past"      
            if nums[right] != nums[right-1]:
                nums[left] = nums[right]
                left += 1
            
        return left