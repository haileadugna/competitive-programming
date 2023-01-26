class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        
        res = ""
        lenwordone = len(word1)
        lenwordtwo = len(word2)
        left, right = 0, 0
        while left < lenwordone and right < lenwordtwo:
            if word1[left] > word2[right]:
                res += word1[left]
                left += 1
            elif word1[left] < word2[right]:
                res += word2[right]
                right += 1
            else:
                if word1[left:] > word2[right:]:
                    res += word1[left]
                    left += 1
                else:
                    res += word2[right]
                    right += 1
        if left < lenwordone:      
            res += word1[left:]
        if right < lenwordtwo:
            res += word2[right:]
        return res