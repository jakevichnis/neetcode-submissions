class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        output = set()
        for i in nums:
            if i in output:
                return True
            output.add(i)
        return False