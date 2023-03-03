class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        def f(temp):
            tmp = list(temp)
            dictt = Counter(tmp)
            return dictt[min(tmp)]
        
        querie = []
        word = []
        for i in range(len(queries)):
            querie.append([f(queries[i]), i])
        
        n = len(words)
        for i in range(n):
            word.append([f(words[i]), i])
        
        querie.sort()
        word.sort()
        res = [0] * len(querie)
        
        for i in range(len(querie)):
            pre = 0
            for j in range(pre, len(word)):
                if querie[i][0] < word[j][0]:
                    pre = j
                    res[querie[i][1]] = n - j
                    break
        # print(querie)
        # print(word)
        return res
    
    """[[1, 0], [2, 4], [2, 5], [2, 6], [2, 8], [3, 9], [4, 3], [6, 2], [6, 7], [7, 1]]
        [[3, 0], [2, 1], [2, 2], [1, 3], [1, 4], [1, 5], [1, 6], [10, 7], [5, 8], [2, 9]]

"""
    
    