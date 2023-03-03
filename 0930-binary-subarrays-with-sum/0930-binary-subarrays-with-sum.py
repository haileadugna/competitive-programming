class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        res = 0
        n = len(nums)
        left = 0
        if nums[-1] == 0 and goal == 0:
            ans = ((n + 1)* n)//2
            return ans        
        
        dictt = {0:1}
        for i in range(len(nums)):
            
            diff = nums[i] - goal
            
            if diff in dictt:
                res += dictt[diff] 
                
            dictt[nums[i]] = 1 + dictt.get(nums[i], 0)
        return res