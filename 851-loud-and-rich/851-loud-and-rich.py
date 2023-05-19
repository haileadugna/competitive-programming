class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        graph = defaultdict(list)
        incoming = [0] * len(quiet)
        for i, j in richer:
            graph[i].append(j)
            incoming[j] += 1
        
        res = [i for i in range(len(quiet))]
        todo = deque([])
        for i in range(len(incoming)):
            if incoming[i] == 0:
                todo.append(i)

        while todo:
            node = todo.popleft()
            temp = quiet[node]
            for child in graph[node]:
                incoming[child] -= 1
             
                if quiet[child] > temp:
                    quiet[child] = temp
                    res[child] = res[node]
                   
                if incoming[child] == 0:
                    todo.append(child)
            # break
        return res