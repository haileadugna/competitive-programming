class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1 :
            return 0
        l = 0
        count = 1
        while l < len(nums)-1:
            if nums[l] + l >= len(nums) -1:
                return count
            r = nums[l]
            if r == 0:
                break
            jumb = 0
            temp = 0
            for i in range(l+1, r+l+1):
                if nums[i] > jumb or i + nums[i] > temp:
                    j = i
                    jumb = nums[i]
                    temp = i + nums[i]
            l = j
            jumb = 0
            count += 1
        