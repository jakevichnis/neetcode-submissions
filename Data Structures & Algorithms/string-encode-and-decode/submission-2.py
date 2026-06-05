class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) <= 0:
            return ""
        output = ""
        for i in strs:
            output += f"{len(i)}#{i}"
        return output
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        result = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            number = int(s[i:j])
            width = s[j+1:j + 1 + number]
            result.append(width)
            i = j + 1 + number
        return result