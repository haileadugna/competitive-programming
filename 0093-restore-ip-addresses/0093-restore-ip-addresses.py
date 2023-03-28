class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        res = []
        if len(s) > 12:
            return res
        
        def backtracking(i, dot, cur):
            if dot == 4 and i == len(s):
                res.append(cur[:-1])
                return
            if dot > 4:
                return
            for j in range(i, min(len(s), i + 3)):
                if int(s[i:j+1]) < 256 and (i == j or s[i] != "0"):
                    backtracking(j + 1, dot + 1, cur + s[i:j+1] + ".")
        backtracking(0, 0, "")            
        return res