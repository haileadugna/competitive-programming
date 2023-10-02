
class Solution:
    

    def startsWith(self, prefix: str) -> bool:
        cur = self._set
        temp = ""
        res = 0
        for c in prefix:
            temp += c
            if temp in cur:
                res += cur[temp]
            
        return res
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        self.count = Counter(words)
        self._set = defaultdict(int)
        for w in words:
            for c in range(1, len(w) +1):
                self._set[w[:c]] += 1
        # print(self._set)       
        # print(self.count)

        
        ans = []
        for word in words:
            
            res = self.startsWith(word)
                
            ans.append(res)
            
        return ans