class MedianFinder:

    def __init__(self):
        self.heap_add = []
        self.remove = 0
        self.add = 0
        self.heap_removed = []

    def addNum(self, num: int) -> None:
        # print(self.heap_add, self.add)
        # print(self.heap_removed, self.remove)
        if len(self.heap_add) == 0 or self.heap_add and num >= self.heap_add[0]:
            heapq.heappush(self.heap_add, num)
            self.add += 1
            # temp = (self.add)// 2
            # rem = temp - self.remove
            while  self.remove + 1 < self.add :
                removed = heapq.heappop(self.heap_add)
                self.add -= 1
                heapq.heappush(self.heap_removed, -removed)
                self.remove += 1
                # rem -= 1
        else:
            heapq.heappush(self.heap_removed, -num)
            self.remove += 1
            # temp = (self.remove + 2)// 2
            # rem = temp - self.add
          
            while  self.remove > self.add :
                removed = heapq.heappop(self.heap_removed)
                self.remove -= 1
                heapq.heappush(self.heap_add, -removed)
                self.add += 1
                # rem -= 1
        
        

    def findMedian(self) -> float:
        # if self.add == 3:
        #     return self.nums[1]
        if (len(self.heap_add) + len(self.heap_removed)) % 2 == 1:
            return self.heap_add[0]
        # if self.heap_removed and self.heap_add:
        return ( -self.heap_removed[0] + self.heap_add[0])/2
        # return 0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()