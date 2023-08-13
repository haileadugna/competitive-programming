class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        
        n = len(nums)
        dp = [-1]*n
        
        def fuct(nums, i, dp):
                       
            if i == n:
                return True
            
            if dp[i] != -1:
                return dp[i]
            
            if i + 1 < n and nums[i+1] == nums[i]:
               
                if fuct(nums, i + 2, dp):
                    dp[i] = True
                    return True
                    
                if i + 2 < n and nums[i+2] == nums[i]:
                   
                    if fuct(nums, i + 3, dp):
                        dp[i] = True
                        return True
                    
            if i + 2 < n and nums[i] == nums[i + 1] - 1 and nums[i] == nums[i+ 2] -2:
                
                
                if fuct(nums, i + 3, dp):
                    dp[i] = True
                    return True
                    
            dp[i] = False
            return False
        # fuct(nums, 0, dp)
        # print(dp)
        return fuct(nums, 0, dp)