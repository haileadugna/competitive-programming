class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        count = defaultdict(int)
        
        for edge in edges:
            count[edge[0]] += 1
            count[edge[1]] += 1
            
        n = len(count)
        for i in list(count.keys()):
            if count[i] == n - 1:
                return i