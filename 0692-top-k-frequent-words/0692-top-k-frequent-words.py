class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        index = {}
        for i in range(len(words)):
            if words[i] in index:
                continue
            else:
                index[words[i]] = i
                
        count = Counter(words)
        word = []
        
        for ele in list(count.keys()):
            word.append(((count[ele])* -1, ele))
            
        heapq.heapify(word)
        res = []
        while k > 0:
            res.append(heapq.heappop(word))
            k -= 1

        result = []
        for resu in res:
            result.append(resu[1])
            
        return result
        
        