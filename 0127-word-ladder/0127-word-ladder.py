class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordList=set(wordList)
        if endWord not in wordList:
            return 0
        q=deque()
        q.append((beginWord,1))
        while q:
            word,step=q.popleft()
            for i in range(len(beginWord)):
                for j in range(26):
                    new=word[:i]+chr(97+j)+word[i+1:]
                    if new==endWord:
                        return step+1
                    if new in wordList:
                        q.append((new,step+1))
                        wordList.remove(new)
        return 0
#         n = len(beginWord)
       
#         graph = defaultdict(list)
        
#         wordstart = wordList
#         if beginWord not in wordstart:
#             wordstart.append(beginWord)
            
#         def check(start, end):
#             cnt = 0
#             for i in range(n):
#                 if start[i] != end[i]:
#                     cnt += 1

#             if cnt == 1:
#                 return True
#             else:
#                 return False
            
#         for word in wordstart:            
#             for end in wordList:
#                 if check(word, end):
#                     graph[word].append(end)
#                     # graph[end].append(word)

#         # print(graph)
#         stack = [(beginWord, 1)]
#         visited = set([beginWord])
        
#         res = float('inf')
#         while stack:
#             steps = stack.pop()
#             if steps[0] == endWord:
#                 res = min(res, steps[1])
            
#             step = steps[1] + 1
#             for word in graph[steps[0]]:
#                 if word not in visited:
#                     stack.append((word, step))
#                     visited.add(word)
                    
#                 # print(stack)
            
#         return res if res != float('inf') else 0
        
    