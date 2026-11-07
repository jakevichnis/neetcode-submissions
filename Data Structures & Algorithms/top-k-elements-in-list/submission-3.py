from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = Counter(nums)
        buckets = [0] * (len(nums) + 1)

        for num, freq in counter.items():
            if buckets[freq] == 0:
                buckets[freq] = [num]
            else:
                buckets[freq].append(num)

        output = []
        for i in range(len(nums), -1, -1):
            if buckets[i] != 0:
                output.extend(buckets[i])
            if len(output) == k:
                break    
        return output