class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = []
        for i in range(len(matrix)):
            for j in matrix[i]:
                nums.append(j)
        end = len(nums) -1
        start = 0
        if len(nums) == 1:
            if target == nums[0]:
                return True
            else:
                return False
        while start <= end:
            mid = (end + start)//2
            if target == nums[mid]:
                return True
                break
            else:
                if target < nums[mid]:
                    end = mid -1
                else:
                    target > nums[mid]
                    start = mid+1
        else:
            return False
            
                