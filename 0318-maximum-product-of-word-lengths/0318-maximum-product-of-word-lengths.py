class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # print(ord("aa"))
        
        bit = []
        for word in words:
            temp = [0] * 26
            for w in word:
                t = ord(w) - 97
                temp[t] = 1
                
            bit.append(temp)
        
        # print(bit)
        res = 0
        
        for i in range(len(bit) - 1):
            for j in range(i + 1, len(bit)):
                flag = False
                for l in range(26):
                    if (bit[i][l] == 1) and (bit[j][l] == 1):
                        flag = True
                        break
                        
                if not flag:
                    # print("here")
                    res = max(res, len(words[i]) * len(words[j]))
                    
        return res
                
        
        
        
        
        
        
        """
        [[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0], 
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        """