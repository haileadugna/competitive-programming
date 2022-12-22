class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = []
        loser = []
        for i in range(len(matches)):
            winner.append(matches[i][0])
            loser.append(matches[i][1])
        winner.sort()
        loser.sort()
        stack = []
        l, r = 0, 0
        while l < len(winner) and r < len(loser):
            if winner[l] < loser[r]:
                stack.append(winner[l])
                l += 1  
            elif winner[l] > loser[r]:  
                r += 1
            else:
                l += 1
        while l < len(winner):
            stack.append(winner[l])
            l += 1
        ans = sorted(set(stack))
        lose = Counter(loser)
        temp = sorted(set(loser))
        tmp = []
        for num in temp:
            if lose[num] == 1:
                tmp.append(num)
        return [ans, tmp]