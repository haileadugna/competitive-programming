
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        dictstr = defaultdict(list)
        n = len(strs)
        m = len(strs[0])

        i = 0
        while i < m:
            j =0
            while j < n:
                dictstr[i].append(strs[j][i])
                j += 1
            i += 1
        ans = 0
        for l in range(m):
            if dictstr[l] != sorted(dictstr[l]):
                ans += 1
        return ans