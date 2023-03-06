class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.max = 1
        self.element = self.persons[0]
        self.winner = {self.persons[0]: 1}
        self.temp = [-1]*(len(self.persons))
        self.temp[0] = self.persons[0]
        for ind in range(1,len(self.persons)):
            cur_element = self.persons[ind]
            self.winner[cur_element] = 1 + self.winner.get(cur_element,0)
            if self.winner[cur_element] >= self.max:
                self.max = self.winner[cur_element]
                self.element = cur_element 
            self.temp[ind] = self.element 
            
    def q(self, t: int) -> int:
        
        
        ind = bisect.bisect_left(self.times, t)
        if ind == len(self.times):
            return self.temp[-1]
        
        if self.times[ind] > t:
            ind -= 1

        return self.temp[ind]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)