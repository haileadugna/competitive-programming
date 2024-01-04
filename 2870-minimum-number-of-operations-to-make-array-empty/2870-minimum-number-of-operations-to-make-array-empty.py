class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        count = Counter(nums)
        # print(count)
        res = 0
        
        for key in count:
            if count[key] == 1:
                return -1
            
            res += math.ceil(count[key]/3)
            # print(res)
        return res