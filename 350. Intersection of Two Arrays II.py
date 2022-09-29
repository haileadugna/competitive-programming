class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        ans = []
        s, r, t, e = 0, 0, len(nums1)-1, len(nums2)-1
        while s <= t and r <= e:
            if nums1[s] == nums2[r]:
                ans.append(nums1[s])
                s += 1
                r += 1
            elif nums1[s] > nums2[r]:
                r += 1
            else:
                s += 1
        return ans
            