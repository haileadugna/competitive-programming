class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.endWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        
        cur = self.root
        # print(cur.children)
        for c in word:
            if c not in cur.children :
                cur.children[c] = TrieNode()
                
            cur = cur.children[c]
        cur.endWord = True

    def search(self, word: str) -> bool:
        
        
        def dfs(i, root):
            cur = root

            for c in range(i, len(word)):
                
                if word[c] == ".":           
                    for child in cur.children.values():
                        if dfs(c +1, child):
                            return True
                    return False
                
                else:
                    if word[c] not in cur.children:
                        return False
                    cur = cur.children[word[c]]

            return cur.endWord
        
        return dfs(0, self.root)
    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)