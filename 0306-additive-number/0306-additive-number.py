class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        def additive(num, path):
            if len(path) >= 3 and int(path[-3]) + int(path[-2]) != int(path[-1]):
                return 
            if num == "" and len(path) >= 3:
                return True
            for i in range(1, len(num) + 1):
                cur_num = num[:i]
                if len(cur_num) > 1 and cur_num[0] == "0":
                    return
                path.append(cur_num)
                temp = additive(num[i:], path)
                if temp:
                    return True
                path.pop()
        return additive(num, [])
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def run(i, alist, ans):
#             if len(alist) >= 3 and int(alist[-3]) + int(alist[-2]) == int(alist[-1]):
#                 ans.append(True)
#                 return
#             else:
#                 ans.append(False)
#                 return
            
            
#             for ind in range(i, len(num)):
#                 # print(alist)
#                 alist.append(num[i:ind + 1])
#                 temp = run(ind + 1, alist, ans)
                
#                 if temp:
#                     return True
#                 alist.pop()
                  
#         return run(0, [], [])