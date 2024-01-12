class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        lenth = len(s)
        n = lenth//2
        
        counta =0
        countb = 0
        for i in range(len(s)):
            if i < n and  s[i] in vowels:
                counta += 1
            else:
                if s[i] in vowels:
                    countb += 1
        if counta == countb:
            return True
        return False