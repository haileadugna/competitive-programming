class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        start, end = 0, len(arr)-1
        
        while start <= end:
            mid = (start + end)//2
            if arr[mid] >= arr[mid-1] and arr[mid] >= arr[mid +1] :
                return mid
                break
                
            elif arr[mid] < arr[mid-1] and arr[mid] >= arr[mid +1] :
                end = mid
            else:
                start = mid