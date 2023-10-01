class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        word = set(words)
        words.sort(key = lambda c:(-len(c), c))
        # print(words)
        for w in words:
            n = len(w) -1
            for k in range(1, len(w)):
                
                if w[:k] in word:
                    n -=1
            if n == 0:
                return w

        return ""