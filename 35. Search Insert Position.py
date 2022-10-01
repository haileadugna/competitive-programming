class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (end + start)//2
            if target == nums[mid]:
                return mid
                break
            else:
                if target < nums[mid]:
                    end = mid -1
                else:
                    start = mid+1
        return start