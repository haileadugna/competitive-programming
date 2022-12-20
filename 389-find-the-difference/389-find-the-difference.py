class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = Counter(s)
        for i in t:
            if i in s and s[i] > 0:
                s[i] -= 1
            elif i not in s or s[i] == 0:
                return i
            