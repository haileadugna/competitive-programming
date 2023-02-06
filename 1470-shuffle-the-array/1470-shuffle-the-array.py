class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # initialize an empty list to store the shuffled result
        res = []
        # find the length of first half of the input list
        temp = len(nums)//2
        # loop through the first half of the input list
        for i in range(len(nums)//2):
            # add the current element from the first half to the result list
            res.append(nums[i])
            # add the corresponding element from the second half to the result list
            res.append(nums[i + temp])
        # return the shuffled result
        return res
