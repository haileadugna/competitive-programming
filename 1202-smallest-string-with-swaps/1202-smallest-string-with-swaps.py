class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
       
        parent = {}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
                
            return parent[x]
        
        def union(x,y):
            xroot = find(x)
            yroot = find(y)
            
            if rank[xroot] < rank[yroot]:
                parent[xroot] = yroot
            elif rank[xroot] > rank[yroot]:
                parent[yroot] = xroot
            else:

                parent[yroot] = xroot
                rank[xroot] += 1
         
                    
        def sortString(string):
            chars = list(string)
            chars.sort()
            return ''.join(chars)

        rank = [0]* len(s)
        # Step 1: Initialize parent and rank
        for i in range(len(s)):
            parent[i] = i
            
        
        # Step 2: Perform unions based on the given pairs
        for pair in pairs:
            union(pair[0], pair[1])
        
        # Step 3: Group characters based on their parent roots
        groups = defaultdict(list)
        for i in range(len(s)):
            groups[find(i)].append(s[i])
        
        # Step 4: Sort characters in each group
        for key in groups:
            groups[key] = list(sortString(groups[key]))
        # print(groups)
        # Step 5: Reconstruct the string based on the sorted groups
        result = []
        for i in range(len(s)):
            result.append(groups[find(i)].pop(0))
        
        return "".join(result)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    