class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        temp = {}
        for ele in range(len(names)):
            temp[heights[ele]] = names[ele]
            
        maxlen = max(heights)+1
        temparr = [0]*maxlen
        for i in heights:
            temparr[i] += 1
        
        res = []
        for j in range(maxlen):
            if temparr[j] == 0:
                continue
            else:
                for l in range(temparr[j]):
                    res.append(j)
     
        ans = []
        for height in res:
            ans.append(temp[height])  
        ans.reverse()
        return ans
        
#         for i in range(len(heights)):
#             flag = True
#             for j in range(len(heights)-1-i):
#                 if heights[j] < heights[j+1]:
#                     heights[j], heights[j+1] = heights[j+1] , heights[j]
#                     names[j], names[j+1] = names[j+1], names[j]
#                     flag = False
#             if flag :
#                 break

#         return names

        # for i in range(len(heights)):
        #     ind = i
        #     pev = heights[i]
        #     for j in range(i, len(heights)):
        #         if heights[j] < pev:
        #             ind = j
        #             pev = heights[j]
        #     heights[ind], heights[i] = heights[i], heights[ind]
        #     names[ind], names[i] = names[i], names[ind]
        # names.reverse()
        # return names
        
#         for i in range(1, len(names)):
#             if heights[i] < heights[i-1]:
#                 start = i
#                 while heights[start] > heights[start-1]:
#                     heights[start], heights[start-1] = heights[start-1] ,heights[start]
#                     names[start], names[start-1] = names[start-1], names[start]
#                     start -= 1
                    
#         return names

            
            
    