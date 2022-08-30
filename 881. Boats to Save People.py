class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        start = 0
        end = len(people) -1
        ans = 0
        while start <= end:
            if people[end] == limit:
                end -=  1
                ans +=1
            elif people[end] + people[start] <= limit:
                end -= 1
                start += 1
                ans += 1
            elif people[end] + people[start] > limit:
                end -= 1
                ans += 1
        return ans
                