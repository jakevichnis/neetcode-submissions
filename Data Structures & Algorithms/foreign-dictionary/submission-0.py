class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {char:set() for word in words for char in word}
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            minLen = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""
            for j in range(minLen):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break
        visit = {} # False=visited, True=visited & current path
        result = []

        def dfs(char):
            if char in visit:
                return visit[char]
            visit[char] = True
            for neighbor in adj[char]:
                if dfs(neighbor):
                    return True
            visit[char] = False
            result.append(char)
        for char in adj:
            if dfs(char):
                return ""
        result.reverse()
        return "".join(result)