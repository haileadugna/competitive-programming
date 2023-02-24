class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        left = 0
        right = 1
        mid = 0
        res = 1
        dictt = {}
        
        for i in range(len(fruits)):
            if fruits[i] not in dictt:
                dictt[fruits[i]] = 1
            else:
                dictt[fruits[i]] += 1
            if len(dictt) <= 2:
                res = max(sum(list(dictt.values())), res)
            while len(dictt) == 3:
                if dictt[fruits[left]] == 1:
                    del dictt[fruits[left]]
                else:
                    dictt[fruits[left]] -= 1
                left += 1
        return res
                        
    
    
    
    
    
    