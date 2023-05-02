class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # print(hasApple[0])
        graph = defaultdict(list)
        for child, par in edges:
            graph[child].append(par)
            graph[par].append(child)
            
        def dfs(cur, par):
            res = 0
            for child in graph[cur]:
                if child == par:
                    continue
                    
                count = dfs(child, cur)
                if count or hasApple[child]:
                    res += 2 + count
                    # print(res)
                    
            return res
        return dfs(0, -1)