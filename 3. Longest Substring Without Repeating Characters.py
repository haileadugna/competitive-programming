class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = []
        ans = 0
        start = 0
        for i in range(len(s)):
            while s[i] in temp:
                temp.remove(s[start])
                start += 1
            temp.append(s[i])
            ans  = max(i - start +1, ans)
        return ans