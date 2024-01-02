class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        cnt = Counter(nums)
        
        res = []
        for i in range(max(cnt.values())):
            temp = []
            for key in cnt:
                if cnt[key] > 0:
                    temp.append(key)
                    cnt[key] -= 1
                    
            res.append(temp)
            
        return res