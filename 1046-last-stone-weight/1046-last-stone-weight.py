class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones.sort()
        
        while len(stones) > 1:
            
            num1 = stones.pop()
            num2 = stones.pop()
            
            if num1 == num2:
                continue
                
            else:
                dif = num1 - num2
                ind = bisect_left(stones, dif)
                stones.insert(ind, dif)
                
        # print(stones)
        if stones == []:
            return 0
        return stones[0]