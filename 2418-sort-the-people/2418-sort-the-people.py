class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

#         for i in range(len(heights)-1,-1,-1):
#             for j in range(len(heights)-2-i,-1,-1):
#                 if heights[j] < heights[j+1]:
#                     heights[j], heights[j+1] = heights[j+1] , heights[j]
#                     names[j], names[j+1] = names[j+1], names[j]

#         return names

        for i in range(len(heights)):
            ind = i
            pev = heights[i]
            for j in range(i, len(heights)):
                if heights[j] < pev:
                    ind = j
                    pev = heights[j]
            heights[ind], heights[i] = heights[i], heights[ind]
            names[ind], names[i] = names[i], names[ind]
        names.reverse()
        return names