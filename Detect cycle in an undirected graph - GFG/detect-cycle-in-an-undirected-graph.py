from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		graphs = adj
		visited = set()
		colors = [0] * V
        def hasCycle(cur_node, parent):
            colors[cur_node] = 1

            for neighbor in adj[cur_node]:
                if colors[neighbor] == 0:
                    if hasCycle(neighbor, cur_node):
                        return True
                elif colors[neighbor] == 1 and neighbor != parent:
                    return True

            colors[cur_node] = 2
            return False
        
        for i in range(V):
            if colors[i] == 0:
                if hasCycle(i, -1):
                    return True

        return False 

#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends