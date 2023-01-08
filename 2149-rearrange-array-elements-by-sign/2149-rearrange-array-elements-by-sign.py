class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        [1,2,3,4,-1,-2,-3,-4]
        res = []
        even = []
        odd = []
        for num in nums:
            if num > 0:
                even.append(num)
            else:
                odd.append(num)
        for i in range(len(even)):
            res.append(even[i])
            res.append(odd[i])
        return res





#         for i in range(len(nums)-1,-1,-1):
#             if i%2 == 1 and nums[i] > 0:
#                 ind = i 
#                 while nums[ind] > 0 and ind > 0:
#                     ind -= 1

#                 temp = nums[i]
#                 nums[i] = nums[ind]
#                 nums[ind] = temp

#             if i % 2== 0 and nums[i] < 0:
#                 ind = i 
#                 while nums[ind] < 0 and ind > 0:
#                     ind -= 1

#                 temp = nums[i]
#                 nums[i] = nums[ind]
#                 nums[ind] = temp
#             else:
#                 continue
#         return nums