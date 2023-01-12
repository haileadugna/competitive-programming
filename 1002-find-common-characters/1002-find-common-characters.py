class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        shortword = words[0]
        for i in words:
            if len(i) < len(shortword):
                shortword = i
                
        for i in shortword:
            count = 0
            for word in words:
                
                if i in word:
                    count += 1
            if count == len(words):
                res.append(i)
        ans = Counter(res)       
        for word in words:
            temp = Counter(word)
            for ele in res:
                ans[ele] = min(temp[ele], ans[ele])
                
        finalres = []
        listres = list(set(res))
        for i in listres:
            for j in range(ans[i]):
                finalres.append(i)
                
        return finalres