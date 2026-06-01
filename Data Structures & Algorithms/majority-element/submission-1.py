class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        output = {}
        highest_number = 0
        top_key = None
        for i in nums:
            output[i] = output.get(i, 0) + 1
        for key, count in output.items():
            if count > highest_number:
                highest_number = count
                top_key = key
        return top_key