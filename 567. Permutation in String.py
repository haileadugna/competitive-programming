class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        temp = Counter(s1)
        s, e = 0, len(s1)
        while e <= len(s2):
            ans = Counter(s2[s:e])
            if ans == temp:
                return True
            else:
                s += 1
                e += 1
        return False