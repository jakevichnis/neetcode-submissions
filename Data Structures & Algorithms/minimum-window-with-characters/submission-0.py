class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        countT = {}
        for i in range(len(t)):
            countT[t[i]] = countT.get(t[i], 0) + 1
        # empty map for current window
        window = {}
        # chars that currently meet required count
        have = 0
        need = len(countT)
        # store best window
        res = [-1, -1]
        resLen = float("infinity")
        left = 0
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            if s[right] in countT and countT[s[right]] == window[s[right]]:
                have += 1
            # window is valid
            while have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        left, right = res
        return s[left:right+1] if resLen != float("infinity") else ""