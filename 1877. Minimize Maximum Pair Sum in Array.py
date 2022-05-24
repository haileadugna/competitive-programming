class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        summ=[]
        n=len(nums)-1
        for i in range(n+1):
            temp=nums[i]+nums[n-i]
            summ.append(temp)
        ans=max(summ)
        return ans
        