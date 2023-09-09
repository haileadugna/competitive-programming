class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        def backtrack(start, comb, total):
            if total == target:
                res.append(comb.copy())
                return 
            if start >= n or total > target:
                return
            comb.append(candidates[start])
            backtrack(start, comb, total + candidates[start])
            comb.pop()
            backtrack(start+1, comb, total)
        backtrack(0, [], 0)
        return res