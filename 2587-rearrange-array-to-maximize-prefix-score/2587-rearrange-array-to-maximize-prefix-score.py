class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        nums.insert(0, 0)
        temp = -1
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            if nums[i] <= 0 :
                temp = i
                break        
        if temp == -1:
            return len(nums) - 1
        return temp - 1