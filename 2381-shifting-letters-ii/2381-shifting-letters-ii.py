class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        string = []
        for ele in s:
            string.append(ord(ele))
            
        res = [0]*( len(s) + 1)
        for shift in shifts:
            if shift[2] == 1:
                res[shift[0]] += 1
                res[shift[1] + 1] -= 1
            else:
                res[shift[0]] -= 1
                res[shift[1] + 1] += 1
        
        res.pop()
        for i in range(1, len(res)):
            res[i] += res[i-1]
         
        ans = ""
        for j in range(len(string)):
            ans += chr(97 + ((string[j] + res[j]) - 97) % 26)

        return ans