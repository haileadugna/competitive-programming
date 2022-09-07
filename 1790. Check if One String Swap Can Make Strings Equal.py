class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)
        if s1 == s2:
            return True
        if Counter(s1) == Counter(s2):
            count = 0
            for i, j in zip(s1, s2):
                if i !=j:
                    count +=1
            if count == 2 or count == 0:
                return True
        return False
            