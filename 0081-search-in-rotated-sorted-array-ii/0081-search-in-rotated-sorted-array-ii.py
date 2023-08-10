class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        n = len(nums)
        
        left = 0
        right = n -1
        
        if n == 1 :
            return nums[0] == target
        
        while left <= right:
            
            while left < right and nums[right -1] == nums[right]:
                right -= 1
                
            while left < right and nums[left + 1] == nums[left]:
                left += 1
            mid = (left + right)//2
            
            if nums[mid] == target:
                return True
            
            elif nums[mid] < nums[right]:
                if nums[mid] <= target and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            else:
                if nums[mid] >= target and nums[left] <= target:
                    right = mid - 1
                else:
                    left = mid + 1
                                    
                
        return False

                