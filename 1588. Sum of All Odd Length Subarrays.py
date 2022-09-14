class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        temp = [0]*(n+1)
        for i in range(n):
            temp[i+1] += temp[i] + arr[i]
        for j in range(n):
            for k in range(j+1, n+1):
                if (k-j)%2:
                    ans += temp[k] - temp[j]
        return ans