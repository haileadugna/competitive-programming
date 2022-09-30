class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        temp = []
        # for i in range(len(nums1)):
        #     if i < len(nums2):
        #         for j in range(i, len(nums2)):
        #             if nums1[i] <= nums2[j]:
        #                 temp.append([i, j])
        for i in range(len(nums1)):
            s, e = 0, len(nums2) -1
            while s <= e:
                mid  = (s + e)//2
                if nums1[i] <= nums2[mid]:
                    s = mid + 1
                else:
                    e = mid -1
           
            if i  <= e:
                temp.append([i,e])
            s, e = 0, len(nums2) -1
        print(temp)
        ans = 0
        for i in range(len(temp)):
            tmp = temp[i][1] - temp[i][0]
            if tmp > ans:
                ans = tmp
        return ans




