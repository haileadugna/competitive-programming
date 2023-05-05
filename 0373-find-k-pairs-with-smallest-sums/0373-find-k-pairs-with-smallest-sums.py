class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        heap = []
        
        for i in range(min(k, len(nums1))):
            
            for j in range(min(k, len(nums2))):
                
                if len(heap) < k:
                    heapq.heappush(heap, ((nums1[i] + nums2[j])* -1, nums1[i], nums2[j]))
                else:
                    if nums1[i] + nums2[j] > -heap[0][0]:
                        break
                    else:
                        her = heapq.heappop(heap)
                        heapq.heappush(heap, ((nums1[i] + nums2[j])* -1, nums1[i], nums2[j]))
                  
        res = []
        while heap:
            temp = heapq.heappop(heap)
            res.append([temp[1], temp[2]])
        return res