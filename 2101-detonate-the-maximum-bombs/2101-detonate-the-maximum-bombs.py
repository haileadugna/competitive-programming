class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                
                if i == j :
                    continue
                    
                dis = math.sqrt((bombs[i][0] - bombs[j][0])**2 + (bombs[i][1] - bombs[j][1])**2)
                if dis <= bombs[i][2]:
                    graph[i].append(j)

        res = 1
        for source in list(graph.keys()):
            stack = [source]
            visited = set([source])
            while stack:
                node = stack.pop()
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        stack.append(neighbour)
                        visited.add(neighbour )  
            res = max(res, len(visited))
                
        # print(graph)
        return res