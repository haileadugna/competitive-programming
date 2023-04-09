"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
      
        graph = {}
        for employ in employees:
            graph[employ.id] = [employ.importance, employ.subordinates]
        
        stack = deque()
    
        stack.append(id)
        employes = 0
       
        visited = set()
        
        while stack:
            temp = stack.popleft()
            if not temp in visited:
                visited.add(temp)
                employes += graph[temp][0]
                for child in graph[temp][1]:
                    stack.append(child)
                
                
        return employes