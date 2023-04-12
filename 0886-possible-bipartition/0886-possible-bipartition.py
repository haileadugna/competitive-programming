class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for like in dislikes:
            graph[like[0]].append(like[1])
        
        set1 = set()  # set of nodes in one partition
        set2 = set()  # set of nodes in the other partition
        visited = set()  # set of visited nodes
        queue = deque()  # queue for BFS traversal

        # start at an arbitrary node and add it to set1
        for i in range(1, n + 1):
            set1 = set()  # set of nodes in one partition
            set2 = set()  # set of nodes in the other partition
            visited = set()  # set of visited nodes
            queue = deque()  # queue for BFS traversal
            start_node = i
            set1.add(start_node)
            visited.add(start_node)
            queue.append(start_node)

            while queue:
                node = queue.popleft()
                neighbors = graph[node]
                # print("here", node)
                # assign neighbors to the other set
                for neighbor in neighbors:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                    if node in set1:
                        set2.add(neighbor)
                    if node in set2:
                        set1.add(neighbor)

            # print(graph)
            # print(set2, set1)
            for num in list(set1):
                if num in set2:
                    return False
        return True