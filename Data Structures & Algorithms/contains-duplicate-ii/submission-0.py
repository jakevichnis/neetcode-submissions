class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashtable = {}
        for i in range(len(nums)):
            if nums[i] in hashtable and (i - hashtable[nums[i]] <= k):
                return True
            hashtable[nums[i]] = i
        return False