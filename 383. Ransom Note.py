class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dictt = {}
        for i in magazine:
            if i in dictt:
                dictt[i] +=1
            else:
                dictt[i] = 1
        print(dictt)
        for j in ransomNote:
            if j not in dictt:
                return False
            elif dictt[j] > 0:
                dictt[j] -= 1
            else:
                return False
        return True