class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        graphs = defaultdict(list)
        incoming = [0] * len(graph)
        terminal = set()
        for i in range(len(graph)):
            if graph[i] != []:
                for edge in graph[i]:
                    graphs[i].append(edge)
                    incoming[edge] += 1
                    
            else:
                terminal.add(i)
          
        # print(graphs)
        
        todo = deque()
        for i in range(len(graph)):
            # if incoming[i] != 0:
            todo.append(i)
          
        colors = [0] * len(graph)
        def hascycle(cur_node, colors):
            if colors[cur_node] == 2:
                return False
            
            if colors[cur_node] == 1:
                return True
            
            colors[cur_node] = 1
            for neighbor in graphs[cur_node]:
                found = hascycle(neighbor, colors)
                if found:
                    return True
                              
                    
            colors[cur_node] = 2
            return False
            
        stack = []
        for node in todo:
            temp = []
            found = hascycle(node, colors)
            if not found:
                stack.append(node)
     
        return sorted(stack)
                
            