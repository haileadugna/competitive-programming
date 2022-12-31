class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res  = ""
        pev = 0
        for i in spaces:
            res += s[pev:i] + " "
            pev = i
        return res + s[pev:]