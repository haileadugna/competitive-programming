class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        if (len(nums) == 1):
            return [nums[:]]

        for i in range(len(nums) ):
            n = nums.pop(0)
            perms = self.permuteUnique(nums)
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        ans = []
        for num in result:
            if num not in ans:
                ans.append(num)
        return ans