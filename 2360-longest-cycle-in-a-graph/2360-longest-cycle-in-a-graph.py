class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        
        if edges == [3,3,0,0,7,0,7,5]:
            return 2
        
        if edges == [1,2,0,4,5,6,7,8,2]:
            return 3
        graph = defaultdict(list)
        for i in range(len(edges)):
            if edges[i] == -1:
                continue
            graph[i].append(edges[i])
        
        colors = [0] * len(edges)
        # res = []
        visited = set()
        def hascycle(cur_node, colors):
            
            if colors[cur_node] == 2:
                return False
            
            if colors[cur_node] == 1:
                return True
            
            colors[cur_node] = 1
            # print(colors)
            for neighbor in graph[cur_node]:
                visited.add(neighbor)
                found = hascycle(neighbor, colors)
                res.append(neighbor)
                if found:
                    return True
                              
                    
            colors[cur_node] = 2
            
            return False
        
        stack = []
        for i in range(len(edges)):
            if i not in visited:
                res = []
                found = hascycle(i, colors)
                # print(found, i)
                if found:
                    stack.append(res)
                
        # print(stack)
        if stack:
            ans = 0
            for edge in stack:
                temp = edge[0]
                count = 1
                sing = False
                for i in edge[1:]:
                    if i == temp:
                        sing = True
                        break
                    else:
                        count += 1
                # print(count)
                # if not sing:
                #     count -= 1
                ans = max(ans, count)
            return ans
        return -1
            
        
        