class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        dictt = [[0, i] for i in range(len(mat))]
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    dictt[i][0] += 1
                    
        dictt.sort()
        res = []
        for i in range(k):
            res.append(dictt[i][1])
            
        return res
                    
                    
        