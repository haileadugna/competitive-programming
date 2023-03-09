class Solution:
    def splitString(self, s: str) -> bool:
        
        def run(i, alist):
            if len(alist) >= 2 and int(alist[-2]) - int(alist[-1]) != 1:
                return False
            elif len(alist) > 1 and len("".join(alist)) == len(s):
                return True
            
            
            for ind in range(i, len(s)):
                # print(alist)
                alist.append(s[i:ind + 1])
                temp = run(ind + 1, alist)
                
                if temp:
                    return True
                alist.pop()
                
        return run(0, [])