class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        for i in range(n):
            graph[i].append(labels[i])
            
        res = [0] * n
        def dfs(node, parent):
            count = [0] * 26
            label = ord(graph[node][-1]) - ord('a')
            count[label] += 1
            for neibr in graph[node][:-1]:
                if neibr != parent:
                    sub_count = dfs(neibr, node)
                    for i in range(26):
                        count[i] += sub_count[i]
            res[node] = count[label]
            return count
            
        dfs(0, -1)
        return res