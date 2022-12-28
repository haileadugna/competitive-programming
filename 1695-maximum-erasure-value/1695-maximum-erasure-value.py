class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        length = len(nums)
        left = 0
        res = 0
        right = 0
        summ = 0
        temp = set()
        for i in range(length):
            while nums[right] in temp:
                temp.remove(nums[left])
                summ -= nums[left]
                left += 1

            temp.add(nums[i])
            summ += nums[i]
            res = max(res, summ)
            right += 1
            
        return res