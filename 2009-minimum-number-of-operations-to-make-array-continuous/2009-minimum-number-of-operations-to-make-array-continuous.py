class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        nums.sort()
        _set = list(set(nums))
        _set.sort()
        n = len(nums)
            
        res = n
        for i in range(len(_set)):
            left = _set[i]
            right = left + n - 1
            j = bisect_right(_set, right)
            count = j - i
            res = min(res, n - count)
        # print(_set, nums)
        
        return res