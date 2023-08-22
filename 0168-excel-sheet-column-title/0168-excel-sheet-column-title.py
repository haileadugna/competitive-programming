class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        res = ""
        while columnNumber > 0:
            remder = (columnNumber -1)%26
            res = chr(remder + 65) + res
            columnNumber = (columnNumber-1) // 26

        return res