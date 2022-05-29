class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums=[]
        nums2.append(-1)
        for i in range(len(nums1)):
            for j in range(len(nums2)-1):
                if nums1[i] != nums2[j]:
                    continue
                elif nums1[i] == nums2[j] and nums1[i] > max(nums2[j+1:]):
                    nums.append(-1)                     
                else:
                    temp = nums2[j:]
                    for k in range(len(temp)):
                        if nums1[i] < temp[k]:
                            nums.append(temp[k])
                            break
        return nums