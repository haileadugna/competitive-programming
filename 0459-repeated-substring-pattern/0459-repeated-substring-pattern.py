class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        tmp = ""
        for i in range(len(s)//2):
            tmp += s[i]
            if len(s)% len(tmp) == 0:
                if tmp * (len(s)// len(tmp)) == s:
                    return True
        return False
            