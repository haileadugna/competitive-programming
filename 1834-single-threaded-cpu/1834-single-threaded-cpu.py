class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for i in range(len(tasks)):
            tasks[i].append(i)
          
        tasks.sort()
        heap =[]
        res = []
        time = tasks[0][0]
        i = 0
        while heap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(heap, tasks[i][1:])
                i += 1
                
            if not heap:
                time = tasks[i][0]
                
            else:
                temp = heapq.heappop(heap)
                time += temp[0]
                res.append(temp[1])
            
        return res