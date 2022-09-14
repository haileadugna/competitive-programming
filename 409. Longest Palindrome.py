class Solution:
    def longestPalindrome(self, s: str) -> int:
        nums = Counter(s)
        num = list(nums.values())
        ans = 0
        for i in num:
            ans += (i//2)*2
            if ans%2 == 0 and i % 2==1:
                ans +=1
        return ans
                
        