class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    # 1) Load all numbers in a set
        output = 0
        array = {x for x in nums}
        for i in array:
            # 2) For each number, check if num - 1 is NOT in the set -- if so, it's a sequence start
            if i - 1 not in array:
            # 3) From that start, count upward while num + 1 exists in the set
                longest = 1
                while i + longest in array:
                    longest += 1
            # 4) Update longest if current streak beats it
                output = max(output, longest)
            else:
                longest = 0
    # 5) return longest
        return output