class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        temp = ["a",'e', 'i', 'o', 'u', "A",'E','I','O','U']
        l, r= 0, len(s)-1
        while l <= r:
            if s[l] in temp:
                while s[r] not in temp and r > l:
                    r -= 1
                    print(r)
                t = s[l]
                s[l] = s[r]
                s[r] = t
                r -= 1
            l += 1
        return "".join(s)

                
                