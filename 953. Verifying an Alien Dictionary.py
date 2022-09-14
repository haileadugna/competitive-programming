class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order2 = {c:i for i, c in enumerate(order)}
        for i in range(len(words)-1):
            wl, w2 = words[i], words[i + 1]
            for j in range(len(wl)):
                if j == len(w2):
                    return False
                if wl[j] != w2[j]:
                    if order2[w2[j]] < order2[wl[j]]:
                        return False
                    break
        return True