class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        
        def isPossible(p, diff):
            i = 1
            while i < n:
                if nums[i] - nums[i-1] <= diff:
                    p -= 1
                    i += 1
                i += 1
                    
            return p <= 0
        
        
        nums.sort()
        left = 0
        right = nums[n-1] - nums[0]
        ans = right
        
        while left <= right:
            mid = (left + right)//2
            
            if isPossible(p, mid):
                ans = mid
                right = mid -1
                
            else:
                left = mid + 1
                
        return ans
            