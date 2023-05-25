class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        
        arr.sort()
        
        if arr[0] != 1:
            arr[0] = 1
            
        for i in range(1, len(arr)):
            if abs(arr[i - 1] - arr[i]) > 1:
                arr[i] = arr[i-1] + 1
        # if len(arr) == 1:
        #     return 1
        # if abs(arr[-1] - arr[-2]) > 1:
        #     arr[-1] = arr[-2] + 1
            
        # print(arr)
        return max(arr)
            