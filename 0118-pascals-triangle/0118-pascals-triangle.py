class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        ans = []
        for i in range(1, numRows+1):
            temp = []
            for j in range(i):
                temp.append(1)
            ans.append(temp)
            
        for k in range(2, numRows):
            for l in range(1, k):
                ans[k][l] = ans[k-1][l-1] + ans[k-1][l] 
                
        return ans
       