class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=[]
        temp={}
        summ=[]
        for ans in nums:
            if ans in temp:
                temp[ans]+=1
            else:
                temp[ans]=1
        for i in temp:
            summ.append([temp[i],i])
        summ.sort(reverse=True)
        for j in range(len(summ[:k])):
            n.append(summ[j][1])
        return n