class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}
        running = 0
        result = 0
        for i in nums:
            running += i
            complement = running - k
            if complement in prefix:
                result += prefix[complement]
            prefix[running] = prefix.get(running, 0) + 1
        return result