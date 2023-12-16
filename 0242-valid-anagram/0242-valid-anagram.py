class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       
        ans1 = Counter(list(s))
        ans2 = Counter(list(t))
        if ans1 == ans2:
            return True
        return False
