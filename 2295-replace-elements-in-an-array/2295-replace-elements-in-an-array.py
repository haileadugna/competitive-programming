class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        dictnums = {}
        for i in range(len(nums)):
            dictnums[nums[i]] = i

        for j in range(len(operations)):
            ind = dictnums[operations[j][0]]
            nums[ind] = operations[j][1]
            dictnums[operations[j][1]] = ind
        return nums