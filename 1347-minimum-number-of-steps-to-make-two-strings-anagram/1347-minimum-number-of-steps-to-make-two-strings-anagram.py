class Solution:
    def minSteps(self, s: str, t: str) -> int:
        scnt = Counter(s)
        tcnt = Counter(t)
        # print(scnt)
        # print(tcnt, "t")
        
        res = 0
        for key in scnt.keys():
            if key in tcnt and tcnt[key] > scnt[key]:
                res += tcnt[key] - scnt[key]
                
        for key in tcnt.keys():
            if key not in scnt:
                res += tcnt[key]
                
                
        return res