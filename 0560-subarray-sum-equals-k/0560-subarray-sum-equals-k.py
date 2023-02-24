class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        d = defaultdict(int)
        temp = 0
        d[0] += 1
        res = 0
        for i in range(len(nums)):
            temp += nums[i]
            r = temp - k
            res += d[r]
            d[temp] += 1

        return res