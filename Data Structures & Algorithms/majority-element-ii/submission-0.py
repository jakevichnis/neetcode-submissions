class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        amount = len(nums) // 3
        hashtable = {}
        output = []
        for i in nums:
            hashtable[i] = hashtable.get(i, 0) + 1
        for j in hashtable:
            if hashtable[j] > amount:
                output.append(j)
        return output