class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()  
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i == j :
                    continue
                else:
                    if arr[i] * 2 == arr[j]:
                        return True
        return False
            
#         j = 0
#         temp = {}
#         for i in range(len(arr)):
#             temp[i] = arr[i]
        
#         print(temp)
#         while j < len(arr) and 2* temp[j] <= arr[-1] :
#             if temp[j] == temp[2*temp[j]]:
#                 j += 1
#             elif 2*arr[j] in arr:
#                 return True
#             else:
#                 j += 1
#         return False