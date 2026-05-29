class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement in dict_:
                return [dict_[complement], index]
            dict_[value] = index
