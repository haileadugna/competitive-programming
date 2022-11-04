class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        temp = Counter(words)
        ans = 0
        l = 0
        for w in temp.keys():
            if w == w[::-1]:
                if temp[w] % 2 == 1:
                    ans = 2
                l += (temp[w]//2*2)*2
            else:
                l += min(temp[w], temp[w[::-1]])*2
        return l + ans
        