class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        if len(arr) < 3:
            return True
        temp = arr[1] - arr[0]
        for i in range(1,len(arr)-1):
            if arr[i+1] - arr[i] == temp:
                pass
            else:
                return False
        return True