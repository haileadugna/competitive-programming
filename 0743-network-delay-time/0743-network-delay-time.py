class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(dict)
        
        for time in times:
            start, target, weight = time
            if start not in graph:
                graph[start] = {}
            graph[start][target] = weight
        
        # print(graph)
        
        start = k
        distances = {node: float('inf') for node in range(1, n + 1)}
        distances[start] = 0
        visited = set()
        
        # print(distances)
        priority_queue = [(0, start)]
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            
            if current_node in visited:
                continue
                
            visited.add(current_node)
            for neighbor, weight in graph[current_node].items():
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        # print(distances)        
        return max(list(distances.values())) if float("inf") not in distances.values() else -1
