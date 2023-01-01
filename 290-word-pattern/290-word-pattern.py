class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dictt = {}
        s = s.split()
        temp = set()
        if len(s) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in dictt :
                if s[i] != dictt[pattern[i]]:
                    return False

            else:
                if s[i] in temp:
                    return False
                else:
                    dictt[pattern[i]] = s[i]
                    temp.add(s[i])

        return True
                    
                
                