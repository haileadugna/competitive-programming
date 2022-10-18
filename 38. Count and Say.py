class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        cur = self.countAndSay(n-1)
        temp = []
        ans = ""
        l =1
        for i in range(len(cur)):
            if i == len(cur) -1 or cur[i] != cur[i+1]:
                ans += str(l) + cur[i]
                l  = 1
            else:
                l += 1
        return ans

