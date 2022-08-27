class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        for num in words:
            if num in freq:
                freq[num] +=1
            else:
                freq[num] = 1
        return sorted(freq.keys(), key = lambda w: (-freq[w], w))[:k]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    