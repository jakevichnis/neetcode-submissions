class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        output = 0
        current = set()
        for right in range(len(s)):
            while s[right] in current:
                current.discard(s[left])
                left += 1
            current.add(s[right])
            if len(current) > output:
                output = len(current)
        return output