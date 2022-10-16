class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        # temp = 0
        # num = 0
        # for i in range(len(nums1)):
        #     if abs(nums1[i] - nums2[i]) > num:
        #         num = abs(nums1[i] - nums2[i])
        #         temp = i
        # tmp = nums1[:]
        # nums1.sort()
        # l, r = 0 , len(nums1)-1
        # while l <= r:
        #     mid = (l + r)//2
        #     if nums1[mid] < nums2[temp]:
        #         l = mid + 1
        #     else:
        #         r = mid -1
        # tmp[temp] = nums1[mid]
        # print(l, r)
        # print(temp)
        # ans = 0
        # print(tmp)
        # for i in range(len(nums1)):
        #     ans += abs(tmp[i] - nums2[i])
        # return ans
        M = 10**9 + 7
        tot = 0
        for i , j in zip(nums1, nums2):
            tot += abs(i - j)
        ans = tot
        temp = list(sorted(nums1))
        for i,  j in zip(nums1, nums2):
            cur = abs(i -j)
            index = bisect.bisect_left(temp, j)
            if 0 <= index < len(temp):
                a = temp[index]
                now = tot - cur + abs(a-j)
                ans = min(ans, now)
            if len(temp) > index -1 >= 0:
                a = temp[index -1]
                now = tot - cur + abs(a-j)
                ans = min(ans, now)
        return ans%M


        