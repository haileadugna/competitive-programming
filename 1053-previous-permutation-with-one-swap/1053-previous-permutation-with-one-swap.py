class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        
        maxx = max(arr)
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] <= arr[i + 1]:
                continue
            else:
                temp = i
                minn = -1
                for j in range(i + 1, len(arr)):
                    if arr[j] > minn and arr[j] < arr[i]:
                        temp = j
                        minn = arr[j]
                        
                arr[i], arr[temp] = arr[temp], arr[i]
                return arr
                    
        return arr