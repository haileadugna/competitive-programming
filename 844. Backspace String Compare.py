class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        tmp1 =[]
        tmp2 = []
        for i in range(len(s)):
            if tmp1 == [] and s[i] == "#":
                continue
            elif s[i] == "#" :
                tmp1.pop()
            else:
                tmp1.append(s[i])
        for j in range(len(t)):
            if tmp2 == [] and t[j] == "#":
                continue
            elif t[j] == "#":
                tmp2.pop()
            else:
                tmp2.append(t[j])
        if tmp1 == tmp2:
            return True
        return False 