class Solution:
    def reorganizeString(self, s: str) -> str:
        
        
        dictt = defaultdict(int)
        
        for c in s:
            dictt[c] += 1
            
        
        heap = []
        for key in dictt.keys():
            heap.append([-dictt[key], key])
            
            
        heapq.heapify(heap)
        
        res = "1"
        print(heap)
        
        while heap:
            if heap[0][1] != res[-1]:
                temp = heapq.heappop(heap)
                # print(heap, temp)
                res += temp[1]
                if temp[0] < -1:
                    heapq.heappush(heap, [temp[0] + 1, temp[1]])
                    
            else:
                if len(heap) > 1:
                    temp1 = heapq.heappop(heap)
                    temp2 = heapq.heappop(heap)
                    res += temp2[1]
                    heapq.heappush(heap, temp1)
                    if temp2[0]  < -1:
                        
                        heapq.heappush(heap, [temp2[0] +1, temp2[1]])
                    
                else:
                    return ''

        return res[1:]
            