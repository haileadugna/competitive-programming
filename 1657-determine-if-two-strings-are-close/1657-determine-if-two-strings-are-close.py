class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1 = Counter(word1)
        word2 = Counter(word2)
        temp1 = word1.values()
        temp2 = word2.values()
        tmp1 = word1.keys()
        tmp2 = word2.keys()
        if (sorted(list(temp1)) == sorted(list(temp2))) and (sorted(list(tmp1)) == sorted(list(tmp2))):
            return True
        return False