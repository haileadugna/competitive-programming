class Solution:
    def decodeString(self, s: str) -> str:
        temp =[]
        for i in range(len(s)):
            if s[i] != "]":
                temp.append(s[i])
            else:
                substr = ""
                while temp[-1]  != "[":
                    substr = temp.pop() + substr
                temp.pop()
                k = ""
                while temp and temp[-1].isdigit():
                    k = temp.pop() + k
                temp.append(int(k)*substr)
                               
        return "".join(temp)