class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s = list(s)
        p = list(p)
        p.sort()
        l, r= 0, len(p)
        ans = []
        while r <= len(s):
            temp = sorted(s[l:r])
            if p == temp:
                ans.append(l)
                l += 1
                r += 1
            else:
                l += 1
                r += 1
        return ans