class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        for i in range(ord("A"), ord("Z")+1):
            left = 0
            ops = k
            target = chr(i)
            for right in range(len(s)):
                while ops <= 0 and s[right] != target:
                    if s[left] != target:
                        ops += 1
                    left += 1
                if s[right] != target:
                    ops -= 1

               
                max_len = max(max_len, right-left+1)
        return max_len