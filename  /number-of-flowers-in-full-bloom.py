class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        
        dictt = {}
        # for i in range(len(people)):
        #     dictt[i] = people[i]
        
        peopl = sorted(people)
        flowers.sort()
        res = [0]* len(people)
            
        heap = []
        
        i = 0
        for peo in peopl:
            
            while i < len(flowers) and flowers[i][0] <= peo:
                heapq.heappush(heap, flowers[i][1])
                
                i += 1
                
                
            while heap and heap[0] < peo:
                heapq.heappop(heap)
                
            dictt[peo] = len(heap)
            # print(heap)
            # print("here", res)
            
        return [dictt[peo] for peo in people]