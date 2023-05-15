class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        incoming = [0] * numCourses
        for i,j in prerequisites:
            graph[j].append(i)
            incoming[i] += 1
            
        todo = deque()
        for i in range(len(incoming)):
            if incoming[i] == 0:
                todo.append(i)
          
        res = []
        while todo:
            node = todo.popleft()
            res.append(node)
            for neibr in graph[node]:
                incoming[neibr] -= 1
                
                if incoming[neibr] == 0:
                    todo.append(neibr)
          
        if len(res) != numCourses:
            return []
                
        return res
                    