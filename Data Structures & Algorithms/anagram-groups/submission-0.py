class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = {}
        for word in strs:

            sorted_word = "".join(sorted(word))
            

            if sorted_word not in buckets:
                buckets[sorted_word] = []
            buckets[sorted_word].append(word)
            
        return list(buckets.values())