class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        for i in range(2, len(nums)):
            j, k =0, i -1
            while j < k:
                if nums[j] + nums[k] > nums[i]:
                    ans += (k - j)
                    k -= 1
                else:
                    j += 1
        return ans