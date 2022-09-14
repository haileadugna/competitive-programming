class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = Counter(list(s))
        tmp = list(s.keys())
        print(tmp)
        t = list(t)
        print(t)
        for i in t:
            if i not in tmp:
                return i
            else:
                if s[i] >= 1:
                    s[i] -= 1
                else:
                    return i