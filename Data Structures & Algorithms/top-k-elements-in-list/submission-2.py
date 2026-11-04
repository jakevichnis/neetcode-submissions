class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        counter = {}
        for i in nums:
            counter[i] = counter.get(i, 0) + 1
        sorted_dict = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
        for i in sorted_dict:
            output.append(i)
        return output[:k]