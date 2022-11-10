class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)-1
        ans = {n:1}
        for i in range(n-1,-1,-1):
            temp = 0
            for j in range(i+1,n+1):
                if nums[i] < nums[j]:
                    temp = max(temp, ans[j])             
            ans[i] = temp + 1
        return max(ans.values())



            