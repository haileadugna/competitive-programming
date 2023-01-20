class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        summ=[0]*3
        length=0
        for j in range(len(nums)):
            summ[nums[j]]+=1
        for k in range(3):
            tempk=summ[k]
            for l in range(length,length+summ[k]):
                #temp.append(k)
                nums[l]=k
            length+=tempk
