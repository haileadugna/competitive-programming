class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        
        ans = []
        
        l, r = 0, 1
        
        temp = []
        temp.append(words[l])
        leng = len(words[l])
        
        while r < len(words):
            
            if len(words[r]) + leng + 1 <= maxWidth:
                temp.append(words[r])
                leng += len(words[r]) + 1
                
                
            else:
                ans.append(temp)
                l = r
                temp = [words[l]]
                leng = len(words[l])
                
            r += 1
            
        if temp != []:
            ans.append(temp)
            
            
        res = []
        for word in ans[:-1]:
            n = len(word) - 1
            size = 0
            sol = []
            
            for w in word:
                size += len(w)
                
            if n == 0:
                sol.append(word[0] + " " * (maxWidth - size))
                
            else:
                
                if (maxWidth - size) % n == 0:

                    t = (maxWidth - size) // n

                    for l in word[:-1]:
                        sol.append(l + " " * t)
                        
                    

                else:
                    t = (maxWidth - size) // n
                    m = (maxWidth - size) % n

                    for l in word[:-1]:
                        if m > 0:
                            sol.append(l + " " * (t + 1))
                            m -= 1
                        else:
                            sol.append(l + " " * (t))
                            
                sol.append(word[-1])
                        
            res.append("".join(sol))  
            
                    
        # for word in ans[-1]:
        n = len(ans[-1]) - 1
        size = 0
        sol = []
        
        for i in ans[-1]:
            size += len(i)

        for w in ans[-1][:-1]:
            sol.append(w + " ")

        sol.append(ans[-1][-1] + " "* (maxWidth - size - n))

        res.append("".join(sol))
                
        return res
                
                