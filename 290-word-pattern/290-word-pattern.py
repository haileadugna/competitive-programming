class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dictt = {}
        s = s.split()
        if len(s) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in dictt :
                if s[i] != dictt[pattern[i]]:
                    return False

            else:
                if s[i] not in dictt.values():
                    dictt[pattern[i]] = s[i]
                else:
                    return False

        return True
                    
                
                