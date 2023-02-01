class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        temp = arr[:]
        maxele = -1
        for i in range(len(arr)-1,-1,-1):
            arr[i] = maxele
            maxele = max(temp[i], maxele)
        return arr
            
        