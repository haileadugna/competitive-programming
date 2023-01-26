class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        temp=[]
        ans=""
        for i in nums:
            temp.append(str(i))
        for k in range(len(temp)):
            for j in range(len(temp)-1):
                start = temp[j] + temp[j+1]
                end = temp[j+1]+temp[j]
                if end>start:
                    temp[j],temp[j+1]=temp[j+1],temp[j]

        return str(int("".join(temp)))