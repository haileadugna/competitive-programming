class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 1
        k = 1
        while r < len(nums):
            if nums[l] != nums[r]:
                l = r
                r += 1
                k += 1
            else:
                nums[r] = "_"
                r += 1
        for i in range(len(nums)-1):
            if nums[i] == "_":
                j = i + 1
                while j < len(nums) and nums[j] == "_":
                    j +=  1
                if j == len(nums):
                    break
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
        n = len(nums)
        while n != k:
            nums.pop() 
            n -= 1     