class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        tickets.sort()
        graph = defaultdict(list)
        for fro, to in tickets:
            graph[fro].append(to)

        res = ["JFK"]
        
        def dfs(node):
            
            if len(res) == len(tickets) + 1:
                return True
            
            if node not in graph:
                return False
            
            temp = list(graph[node])
            for i, val in enumerate(temp):
                graph[node].pop(i)
                res.append(val)
                
                if dfs(val):
                    return True
                
                graph[node].insert(i, val)
                res.pop()
                
            return False
              
        dfs("JFK")
        return res
                
        