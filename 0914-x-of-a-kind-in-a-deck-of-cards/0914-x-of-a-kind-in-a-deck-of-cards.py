class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        count = Counter(deck)
        
        nums = list(count.values())
        
        temp = math.gcd(*nums)
        if temp >= 2:
            return True
        
        return False