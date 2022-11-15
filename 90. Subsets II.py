class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def backtrack(i, subset):
            if i == len(nums):
                ans.append(subset.copy())
                return
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            while i +1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i + 1, subset)
        backtrack(0, [])
        return ans
# second and dumb answer
        
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
        ans = []
        for i in res:
            if sorted(i) not in ans:
                ans.append(sorted(i))
        return ans