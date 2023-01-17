class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        # temp = {}
        # for ele in range(len(names)):
        #     temp[heights[ele]] = names[ele]
            
            
        for i in range(len(heights)):
            for j in range(len(heights)-1):
                if heights[j] > heights[j+1]:
                    heights[j], heights[j+1] = heights[j+1] , heights[j]
                    names[j], names[j+1] = names[j+1], names[j]
               
        # res = []
        # for height in heights:
        #     res.append(temp[height])
        # res.reverse()
        names.reverse()
        return names