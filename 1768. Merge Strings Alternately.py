class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        for i in range(min(len(word1), len(word2))):
            ans += word1[i] + word2[i]
        if len(word1)-1 > i:
            for j in range(i+1, len(word1)):
                ans += word1[j]
        elif len(word2)-1 > i:
            for k in range(i+1, len(word2)):
                ans += word2[k]
        return ans