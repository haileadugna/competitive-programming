class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        s = s.lower()
        while i<=j:
            if (ord(s[i]) < 97 or ord(s[i])>122) and (ord(s[i])<48 or ord(s[i])>57):
                i+=1
                continue
            if (ord(s[j]) < 97 or ord(s[j])>122) and (ord(s[j])<48 or ord(s[j])>57):
                j-=1
                continue
            if s[j] == s[i]:
                j-=1
                i+=1
            elif s[j]!=s[i]:
                return False
        return True