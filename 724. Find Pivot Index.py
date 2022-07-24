class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        temp1 = nums[:]
        n = len(nums)
        for i in range(1, n):
            nums[i] = nums[i-1] + nums[i]
        temp1.reverse()
        for j in range(1, n):
            temp1[j] = temp1[j-1] + temp1[j] 
        temp1.reverse()
        for k in range(len(temp1)):
            if temp1[k] == nums[k]:
                return k
        return -1