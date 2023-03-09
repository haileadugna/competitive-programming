class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        '''
        
                1, 2,3 ,4
                  []
                
        '''
        ans = []
        path = []
        
        def backtrack(start):
            if len(path) == k:
                ans.append(list(path))
                return
            
            if start == n + 1:
                return
            
            backtrack(start + 1)
            
            path.append(start)
            backtrack(start + 1)
            path.pop()
            
            
            
        
        backtrack(1)
        
        return ans