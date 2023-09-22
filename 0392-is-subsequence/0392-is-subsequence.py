class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        count1, count2 = 0,0
        while count1 < len(s) and count2 < len(t):
            if s[count1] == t[count2]:
                count1 += 1
            count2 += 1
        if count1 == len(s):
            return True
        return False