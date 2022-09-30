class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        for i in range(len(nums1)):
            s, e = 0, len(nums2) -1
            while s <= e:
                mid  = (s + e)//2
                if nums1[i] <= nums2[mid]:
                    s = mid + 1
                else:
                    e = mid -1
           
            if i  <= e:
                if e - i > ans:
                    ans = e - i
            s, e = 0, len(nums2) -1
        return ans




