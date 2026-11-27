class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = {}
        for i in range(len(nums)):
            output[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in output and output[complement] != i:
                return [i, output[complement]]
        