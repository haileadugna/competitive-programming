class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        ml , mc = 0,0
        cc = [0]*26
        while r < len(s):
            cc[ord(s[r])- ord("A")] += 1
            mc = max(mc, cc[ord(s[r])- ord("A")])
            while (r- l-mc +1) >k:
                cc[ord(s[l])- ord("A")] -= 1
                l += 1
            ml = max(ml, r-l+1)
            r += 1
        return ml