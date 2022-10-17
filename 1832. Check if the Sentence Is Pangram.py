class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        temp = list(sentence)
        ans = set(temp)
        if 26 == len(ans):
            return True
        else:
            return False