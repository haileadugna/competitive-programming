class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
            
        total = len(nums1) + len(nums2)
        half = (total)//2
        l, r = 0, len(nums2) -1
        
        while True:
            mid = (l + r)//2
            
            j = half - mid - 2
            
            lnums2 = nums2[mid] if mid >= 0 else float("-inf")
            rnums2 = nums2[mid + 1] if mid < len(nums2) -1 else float("inf")
            lnums1 = nums1[j] if j >= 0 else float("-inf")
            rnums1 = nums1[j +1] if j + 1 < len(nums1) else float('inf')
            
            if lnums2 <= rnums1 and lnums1 <= rnums2:
                
                if total%2:
                    return min(rnums2, rnums1)

                return (max(lnums2, lnums1) + min(rnums1, rnums2))/2

            elif lnums2 > rnums1:
                r = mid - 1

            else:
                l = mid + 1
