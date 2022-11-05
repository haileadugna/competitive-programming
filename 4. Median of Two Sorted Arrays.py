class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        temp =[]
        # n = min(len(nums1), len(nums2))
        l, r= 0,0
        while l < len(nums1) and r < len(nums2):
            if nums1[l] < nums2[r]:
                temp.append(nums1[l])
                l += 1
            else:
                temp.append(nums2[r])
                r += 1
        while l < len(nums1):
            temp.append(nums1[l])
            l += 1
        while r < len(nums2):
            temp.append(nums2[r])
            r += 1
        if len(temp)%2 == 1:
            return temp[len(temp)//2]
        else:
            ans = (temp[len(temp)//2-1] + temp[len(temp)//2])/2
            print(temp)
            return ans




