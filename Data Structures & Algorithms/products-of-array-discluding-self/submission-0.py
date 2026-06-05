class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import math
        output = []
        for i in range(len(nums)):
            temp_list = nums.copy() 
            popped_item = temp_list.pop(i)
            result = math.prod(temp_list)
            output.append(result)
        return output
            