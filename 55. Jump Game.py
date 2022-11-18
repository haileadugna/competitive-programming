class Solution:
    def canJump(self, nums: List[int]) -> bool:
        temp = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if nums[i] + i >= temp:
                temp = i
        if temp == 0:
            return True
        return False
