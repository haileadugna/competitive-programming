class Solution:
    def longestPrefix(self, s: str) -> str:
        
        n = len(s)
        for i in range(1, len(s)):
            
            if s[:n -i] == s[i:]:
                return s[:n-i]
            
        return ""