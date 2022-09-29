class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        end = arr[-1]
        ans = []
        tmp = 0
        for i in range(len(arr)):
            if tmp == arr[i]:
                continue
            else:
                while tmp < arr[i]:
                    tmp += 1
                    if tmp in arr:
                        continue
                    else:
                        ans.append(tmp)
        if len(ans) < k:
            cc = k - len(ans)
            for j in range(cc):
                end += 1
            return end
        
        return ans[k-1]
        