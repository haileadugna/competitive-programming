class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        ind = 0
        flag2 = False
        flag = False
        for i in range(1,len(arr)):
            
            if arr[i-1] < arr[i] :
                flag2 = True
                continue
            elif arr[i-1] > arr[i] :
                ind = i
                while ind < len(arr):
                    flag = True
                    if arr[ind-1] > arr[ind]:
                        ind += 1
                    else:
                        return False
            else:
                return False
        if flag and flag2:
            return True
        return False
                