class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n=len(l)
        temp=[]
        ans=[]
        for i in range(n):
            temp.append(nums[l[i]:r[i]+1])
        for j in range(n):
            temp[j].sort()
        for k in temp:
            for l in range(len(k)-2):
                if k[l+2]-k[l+1]!=k[l+1]-k[l]:
                    ans.append(False)
                    break
            else:
                ans.append(True)
        return ans
        
        