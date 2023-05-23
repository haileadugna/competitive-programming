class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
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

        rank = {}
        # Step 1: Initialize parent and rank
        for i in s1:
            parent[i] = i
            rank[i] = 0
        for i in s2:
            parent[i] = i
            rank[i] = 0
        
        # Step 2: Perform unions based on the given pairs
        for i in range(len(s1)):
            union(s1[i], s2[i])
                    
        # Step 3: Group characters based on their parent roots
        groups = defaultdict(list)
        for i in range(len(s1)):
            groups[find(s1[i])].append(s1[i])
            groups[find(s2[i])].append(s2[i])
        
        # Step 4: Sort characters in each group
        for key in groups:
            groups[key] = list(sortString(groups[key]))
        
        # Step 5: Reconstruct the string based on the sorted groups
        result = []
       
        for i in range(len(baseStr)):
            if baseStr[i] not in parent:
                result.append(baseStr[i])
            else:
                temp =  min(groups[find(baseStr[i])])
                result.append(temp)
        # print(result)
        
        return "".join(result)