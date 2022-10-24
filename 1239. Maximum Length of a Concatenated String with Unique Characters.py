class Solution:
    def maxLength(self, arr: List[str]) -> int:
        charser = set()
        def overlap(charser, s):
            c = Counter(charser) + Counter(s)
            return max(c.values()) > 1
        def backtrack(i):
            if i == len(arr):
                return len(charser)
            ans = 0
            if not overlap(charser, arr[i]):
                for c in arr[i]:
                    charser.add(c)
                ans = backtrack(i+1)
                for c in arr[i]:
                    charser.remove(c)
            return max(ans, backtrack(i+1))
        return backtrack(0)
