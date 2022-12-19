class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs[0]) == 0:
            return ""
        ans = ""
        n = 1000
        for l in range(len(strs)):
            if len(strs[l]) < n:
                n = len(strs[l])
        for i in range(n):
            for j in range(len(strs) -1):
                if strs[j][i] != strs[j+1][i]:
                    return ans
            ans += strs[0][i]
        return ans
        