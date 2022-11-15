class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []
        def backtrack(start, comb, target):
            if target == 0:
                res.append(comb.copy())
            if target <= 0:
                return
            prev = -1
            for i in range(start, n):
                if prev == candidates[i]:
                    continue
                comb.append(candidates[i])
                backtrack(i +1, comb, target - candidates[i])
                comb.pop()
                prev = candidates[i]
        backtrack(0, [], target)
        return res