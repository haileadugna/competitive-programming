class Solution:
    def freqAlphabets(self, s: str) -> str:
        temp = {}
        for i in range(1, 10):
            temp[str(i)] = chr(i+ 96)
        for j in range(10, 27):
            temp[str(j) + '#'] = chr(96 + j)
        l = 0
        r = 0
        ans = ""
        while r < len(s):
            if r + 1 < len(s) and s[r+1] == "0" or (r + 2 < len(s) and s[r +2] == "#"):
                ans += temp[str(s[l:r+3])]
                l += 3
                r += 3
            else:
                ans += temp[s[r]]
                r += 1
                l+=1
        return ans