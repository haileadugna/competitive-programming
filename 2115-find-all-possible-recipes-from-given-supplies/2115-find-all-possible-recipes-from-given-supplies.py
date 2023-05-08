class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        graph = defaultdict(list)
        incoming = defaultdict(int)
        for i in range(len(ingredients)):
            for ingre in ingredients[i]:
                graph[ingre].append(recipes[i])
            incoming[recipes[i]] = len(ingredients[i])
                
        queue = deque([])
        for recipe in supplies:
            queue.append(recipe)
            
        # print(queue)
        order = []
        while queue:
            course = queue.popleft()
            
            for neighbor in graph[course]:
                incoming[neighbor] -= 1
                if incoming[neighbor] == 0 :
                    order.append(neighbor)
                    queue.append(neighbor)
                # Why?
      
        return order
        