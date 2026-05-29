class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        dupe = nums.copy()
        ans = nums + dupe
        return ans