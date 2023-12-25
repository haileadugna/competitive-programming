class Solution:
    def numDecodings(self, s: str) -> int:
        
        temp = {len(s):1}
        def dp(i):
            if i in temp:
                return temp[i]
            if s[i] == "0":
                return 0
            ans = dp(i + 1)
            if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")):
                ans  += dp(i + 2)
            temp[i] = ans
            return ans
        return dp(0)