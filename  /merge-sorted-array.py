class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        l = len(nums1) -1
        while n > 0 and m > 0:
            if nums2[n-1] > nums1[m -1] :
                nums1[l] = nums2[n-1]
                l -= 1
                n -= 1
            else:
                nums1[l] = nums1[m-1]
                l -= 1
                m -=1
        if m == 0:
            r = 0
            while r < n:
                nums1[r] = nums2[r]
                r += 1