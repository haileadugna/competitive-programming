class LockingTree:

    def __init__(self, parent: List[int]):
        
        self.parent = parent
        self.temp = [-1]*len(self.parent)
        self.graph = defaultdict(list)
        for i in range(len(self.parent)):
            p = self.parent[i]
            self.graph[p].append(i)
            
        # print(self.graph)
        # print(self.par)
    def lock(self, num: int, user: int) -> bool:
        if self.temp[num] == -1:
            # self.parent[num] = user
            self.temp[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if self.temp[num] == user:
            # self.parent[num] = 0
            self.temp[num] = -1
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        
        const = num
        if self.temp[num] != -1:
            return False
        
        ans = False
        while True:
            if self.temp[num] != -1:
                ans = True
                break
            if num == 0:
                break
            num = self.parent[num]
        
        if ans:
            return False

        ind = []
        def bfs(graph):
            # visited = set()
            queue = deque()
            # visited.add(num)
            queue.append(const)

            while queue:
                node = queue.popleft()
                for key in graph[node]:
                    
                    queue.append(key)
                    if self.temp[key] != -1:
                        ind.append(key)
                        # return True

            # return False
        bfs(self.graph)
        if len(ind) == 0:
            return False
        self.temp[const] = user
        # if const == 0 :
        #     self.temp[0] = user
        for indx in ind:
            self.temp[indx] = -1
        
        return True
        
            



# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)