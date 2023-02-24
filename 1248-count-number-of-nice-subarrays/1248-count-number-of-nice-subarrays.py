class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        count = 0
        res = 0
        
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                nums[i] = 1
            else:
                nums[i] = 0

                
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
            
        