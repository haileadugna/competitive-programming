
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        graph = defaultdict(dict)
        
        for i in range(len(edges)):
            start, target, weight = edges[i][0], edges[i][1], succProb[i]
            if start not in graph:
                graph[start] = {}
            if target not in graph:
                graph[target] = {}
            graph[start][target] = - math.log(weight)
            graph[target][start] = - math.log(weight)
        # print(graph)
        
        start = start_node
        distances = {node: float('inf') for node in range(0, n )}
        distances[start] = 0
        visited = set()
        # visited.add(start)
        
        # print(distances)
        priority_queue = [(0, start)]
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            
            if current_node in visited:
                continue
                
            visited.add(current_node)
            for neighbor, weight in graph[current_node].items():
                distance = current_distance + weight
                # print(distance)
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
            # print(distances)        
        # print(distances, math.exp(distances[end_node]), distances[end_node] == float('inf'))
        if distances[end_node] == float('inf'):
            return 0
        return math.exp(-distances[end_node])
