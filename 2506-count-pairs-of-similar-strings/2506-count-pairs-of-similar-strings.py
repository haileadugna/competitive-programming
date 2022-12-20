class Solution:
    def similarPairs(self, words: List[str]) -> int:
        ans = 0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                temp = sorted(set(list(words[j])))
                temp2 = sorted(set(list(words[i])))
                if temp == temp2:
                    ans += 1
        return ans