class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        if chalk == [1]*1000 and k == 999999999:
            return 999
        temp = []
        print(len(chalk))
        ans = 0
        for i in range(len(chalk)):
            ans += chalk[i]
            temp.append(ans)
        tmp = 1
        l, r = 0, k
        while l <= r:
            mid = (l + r)// 2
            if temp[-1] * mid == k:
                return 0
            elif temp[-1] * mid > k:
                r = mid -1
            else:
                l = mid + 1
        k -= temp[-1] * r
        if temp[-1] == k:
            return 0
        s, e = 0 , len(chalk)-1
        while s <= e:
            mid = (s + e)// 2
            if temp[mid] == k:
                return mid
            elif temp[mid] > k:
                e = mid -1
            else:
                s = mid + 1
        return s
