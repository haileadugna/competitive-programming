class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                summ = sum([nums[i], nums[l], nums[r]])
                if summ == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l-1] == nums[l] and l<r-1:
                        l += 1
                    r -= 1
                    while nums[r+1] == nums[r] and l+1 < r:
                        r -= 1
                elif summ > 0:
                    r -= 1
                    while nums[r+1] == nums[r] and l+1 < r:
                        r -= 1
                else:
                    l += 1
                    while nums[l-1] == nums[l] and l<r-1:
                        l += 1
        return ans
