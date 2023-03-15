class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        def longest(s):
            if len(s) < 2:
                return ""
            ind = -1
            for i in range(len(s)):
                if s[i].islower() and s[i].upper() not in s:
                    ind = i
                    break
                elif s[i].isupper() and s[i].lower() not in s:
                    ind = i
                    break
            if ind == -1:
                return s
            
            return max(longest(s[:ind]), longest(s[ind + 1:]), key = len)
        return longest(s)