class Solution:
    def calculate(self, s: str) -> int:
        
        i, j, res, sign = 0, 0, 0, '+'
        for c in s + '+':
            if c == ' ': continue
            if c.isdigit():
                i = 10 * i + int(c)
                continue
            if sign == '+':
                res += j
                j = i
                
            elif sign == '-':
                res += j
                j = -i
                
            elif sign == '*':
                j = j * i
                
            elif sign == '/':
                j = int(j / i)
            i, sign = 0, c
            
        return res + j