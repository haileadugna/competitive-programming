class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        res = 0
        i = 1
        while i < len(colors):
            if colors[i] != colors[i - 1]:
                i += 1
            else:
                temp = []
                temp.append(neededTime[i-1])
                j = i 
                while j < len(colors) and colors[j] == colors[j-1]:
                    temp.append(neededTime[j])
                    j += 1
                   
                # print(temp)
                i = j +1
                maxx = max(temp)
                res += sum(temp) - maxx
                
        return res