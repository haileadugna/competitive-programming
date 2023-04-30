class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.graph = defaultdict(list)
        self.graph[kingName] = [] 
        self.deaths = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deaths.add(name)

    def getInheritanceOrder(self) -> List[str]:
        visited = []
        def preorder_traversal(graph, start_node):
            if start_node not in self.deaths:
                visited.append(start_node)
            for neighbor in graph[start_node]:
                # if neighbor not in visited:
                preorder_traversal(graph, neighbor)
            # return visited
        preorder_traversal(self.graph, self.kingName)

        return visited
            
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()