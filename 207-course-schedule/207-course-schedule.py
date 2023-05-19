class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        incoming = [0] * numCourses
        for a,b in prerequisites:
            graph[b].append(a)
            incoming[a] += 1
           
        todo = deque()
        visited = set()
        for  i in range(numCourses):
            if incoming[i] == 0:
                todo.append(i)
                visited.add(i)
        # print(todo)
        
        while todo:
            node = todo.popleft()
            
            for child in graph[node]:
                
                incoming[child] -= 1
                
                if incoming[child] == 0:
                    todo.append(child)
                    visited.add(child)
        # print(visited)
        return len(visited) == numCourses
                    
                
        