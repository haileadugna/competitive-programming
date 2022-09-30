class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        start, end = 0, len(s)-1
        while start <= end:
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start += 1
            end -= 1
        ans = ""
        for i in range(len(s)):
            ans += s[i]
        ans = ans.split()
        anss = ""
        for i in range(len(ans)-1,-1,-1):
            anss += ans[i]
            if i != 0:
                anss += " "
        return anss