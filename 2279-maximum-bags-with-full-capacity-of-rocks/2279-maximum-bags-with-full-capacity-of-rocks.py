class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        
        diff = []
        for i in range(len(rocks)):
            diff.append(capacity[i] - rocks[i])
            
        if sum(diff) <= additionalRocks:
            return len(rocks)
        
        diff.sort()
        print(diff)
        res = 0
        i = 0
        while additionalRocks >= diff[i]:
            res += 1
            additionalRocks -= diff[i]
            i += 1
            
        return res