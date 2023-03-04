class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        ans = []
        
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (end + start)//2
            if target == nums[mid]:
                low = mid
                high= mid
                if len(nums) == 1:
                    return [0, 0]
                elif len(nums) == 2:
                    if nums[0] == nums[1]:
                        return [0,1]
                    else:
                        return [mid, mid]
                else:
                    while low > 0 :
                        if nums[low -1] == target:
                            low -=1
                        else:
                            break
                    while  high < len(nums)-1:
                        if nums[high + 1] == target:
                            high += 1
                        else:
                            break 
                    
                    return [low, high]
                break
            else:
                if target < nums[mid]:
                    end = mid -1
                else:
                    target > nums[mid]
                    start = mid+1
        else:
            return [-1 ,-1]