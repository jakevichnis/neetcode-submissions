class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # generate hashmap to store our lookup table
        hashmap = {}
        # iterate through the arrays to get indices
        for i in range(len(nums)):
            # add index to hashmap
            hashmap[nums[i]] = i
        # iterate again through array to get index
        for i in range(len(nums)):
        # create complement variable that will mathematically work out to be the number we look for by subtracting the value we're currently on from the target
            complement = target - nums[i]
            # if the complement is already in the hashmap (we have seen this before) but the index isn't the one we're looking at (aka it's a duplicate)
            if complement in hashmap and hashmap[complement] != i:
                # we return the current index and the index stored in the complement
                return [i, hashmap[complement]]