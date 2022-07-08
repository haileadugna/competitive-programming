class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n-1):
            temp = i
            for k in range(i+1,n):
                if 0 != nums[k]:
                    temp = k
                    break
            if nums[i] == 0 and i != temp:
                a= nums[i]
                nums[i]=nums[temp]
                nums[temp] = a
        return nums