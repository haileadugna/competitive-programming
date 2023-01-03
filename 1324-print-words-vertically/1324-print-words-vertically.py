class Solution:
    def printVertically(self, s: str) -> List[str]:
        strs = s.split()
        length = 0
        for ele in strs:
            length = max(length, len(ele))
        res = []
        for i in range(length):
            temp = []
            for j in range(len(strs)):
                if len(strs[j])<= i:
                    temp.append(" ")
                else:
                    temp.append(strs[j][i])
            for l in range(len(temp)-1,-1,-1):
                if temp[l] != " ":
                    k = l
                    break
            res.append("".join(temp[:k+1]))

        return res
    
    """
    "
    TO
    BE 
    OR 
    NOTT
    TO 
    BE"
    
    
    
    """