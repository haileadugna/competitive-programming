class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        dictt = defaultdict(list)
        
        for i in range(len(s)):
            dictt[s[i]].append(i)
            
        res = -1
        for w in dictt.keys():
            if len(dictt[w]) == 1:
                continue
            else:
                res = max(res, dictt[w][-1] - dictt[w][0] -1)
                
        return res