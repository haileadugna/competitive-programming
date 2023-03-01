class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        temp = Counter(t)
        mx = float('inf')
        l, e= 0, 0
        count = len(temp)
        ans = ""
        while e < len(s):
            while e < len(s) and count != 0:
                if s[e] in temp:
                    temp[s[e]] -= 1
                    if temp[s[e]] ==  0:
                        count -= 1
                e += 1
            while l < e and count == 0:
                if e - l < mx:
                    mx = e - l
                    ans = s[l:e]
                if s[l] in temp:
                    temp[s[l]] += 1
                    if temp[s[l]] > 0:
                        count +=1 
                l += 1
        return ans
            
                
            