class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        maxx = len(arr)
        result = []
        n = len(arr)
        while n > 0:
            for i in range(n-1):
                if arr[i] == maxx:
                    arr = arr[i::-1] + arr[i+1:]
                    result.append(i+1)
                    arr = arr[n-1::-1] + arr[n:]
                    result.append(n)
            maxx -= 1 
            n -= 1
        return result
