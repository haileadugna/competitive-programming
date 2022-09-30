class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans = 0
        for i in range(len(arr1)):
            tmp = 0
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d:
                    break
                else:
                    tmp += 1
            if tmp == len(arr2):
                ans += 1
            else:
                continue
        return ans

                    