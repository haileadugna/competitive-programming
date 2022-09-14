class Solution:
    def toLowerCase(self, s: str) -> str:
        print(ord("a"))
        print(ord("A"))
        ans = ""
        for i in s:
            if ord(i) < 91 and ord(i) > 64:
                ans += chr(ord(i)+ 32)
            else:
                ans += i
        return ans
        