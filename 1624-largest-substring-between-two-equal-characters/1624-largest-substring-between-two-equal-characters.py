class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        dictt = {}
        
        for i in range(len(s)):
            if s[i] not in dictt:
                dictt[s[i]] = i
                
            else:
                res = max(res, i - dictt[s[i]] -1)
                
        return res