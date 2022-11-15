class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # n = len(candidates)
        res = []
        comb = []
        def backtrack(start):
            if start >= len(nums):
                res.append(comb.copy())
                return 
            comb.append(nums[start])
            backtrack(start +1)
            comb.pop()
            backtrack(start+1)
        backtrack(0)
        return res