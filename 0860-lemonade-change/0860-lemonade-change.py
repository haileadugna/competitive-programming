class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        money = defaultdict(int)
        
        for i in range(len(bills)):
            if bills[i] == 5:
                money[5] += 1
            
            elif bills[i] == 10 and money[5] >= 1:
                money[10] += 1
                money[5] -= 1
                
            elif bills[i] == 20:
                if  money[5] >= 1 and money[10] >= 1:
                    money[10] -= 1
                    money[5] -= 1
                    
                elif money[10] == 0 and money[5] >= 3:
                    money[5] -= 3
                    
                else:
                    return False
            else:
                return False
            
        return True
                