class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        seen1 = {}
        seen2 = {}
        left = 0

        # Build seen1 from s1
        for i in s1:
            seen1[i] = seen1.get(i, 0) + 1

        # Build seen2 from the first window of s2
        for i in s2[:len(s1)]:
            seen2[i] = seen2.get(i, 0) + 1

        # If seen1 == seen2 return True
        if seen1 == seen2:
            return True
        # Slide right — add new char, remove left char, update seen2
        for right in range(len(s1), len(s2)):

            seen2[s2[right]] = seen2.get(s2[right], 0) + 1
            seen2[s2[left]] -= 1
            if seen2[s2[left]] == 0:
                del seen2[s2[left]] 
            left += 1
            if seen1 == seen2:
                return True
        return False