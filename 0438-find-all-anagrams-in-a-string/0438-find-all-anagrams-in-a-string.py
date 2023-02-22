class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        dict_str = defaultdict(int)
        for i in p:
            dict_str[i] += 1

        start = 0
        end = len(p)
        cur = defaultdict(int)
        for i in s[:end]:
            cur[i] += 1

        res = []

        while end < len(s):
            if cur == dict_str:
                res.append(start)

            if cur[s[start]] <= 1:
                del cur[s[start]]
            else:
                cur[s[start]] -= 1

            cur[s[end]] += 1

            start += 1
            end += 1
        if cur == dict_str:
            res.append(start)
        return res