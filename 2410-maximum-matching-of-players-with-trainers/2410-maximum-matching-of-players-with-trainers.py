class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        
        players.sort()
        trainers.sort()
        slow = 0
        fast = 0
        res = 0
        
        while fast < len(trainers) and slow < len(players):
            if players[slow] <= trainers[fast]:
                res += 1
                slow += 1
                fast += 1
            
            else:
                fast += 1
        
        return res
       