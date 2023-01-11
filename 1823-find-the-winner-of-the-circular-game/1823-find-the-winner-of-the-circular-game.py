class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        friends = []
        for i in range(n, 0 , -1):
            friends.append(i)
        while len(friends) != 1:
            for i in range(k-1):
                friends.insert(0,friends.pop())
            friends.pop()
            
        return friends[0]
        