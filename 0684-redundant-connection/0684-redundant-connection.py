class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        ans = True
        # n = len(equations)
        parent = {}
       
        for i in range(1001):
            parent[i] = i
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            xroot = find(x)
            yroot = find(y)
            
            if xroot == yroot:
                return
            parent[yroot] = xroot
            
        def isConnected(x,y):
            return find(x) == find(y)
        
                        
        for x, y in edges:
            if isConnected(x, y):
                return [x, y]
            else:
                union(x, y)
                
        # return ans 