class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if abs(i -j) > k:
        #             break
        #         elif nums[i] == nums[j] and abs(i-j) <= k:
        #             return True
        # return False
        temp = {}
        for ind, val in enumerate(nums):
            if  val in temp and abs(ind - temp[val] <= k):
                return True 
            temp[val] = ind
        return False


        