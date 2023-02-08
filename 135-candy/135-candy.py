class Solution:
    def candy(self, ratings: List[int]) -> int:
        temp = [1]*len(ratings)
        add = len(ratings)-2
        i = 1
        while i < len(ratings):
            if ratings[i] > ratings[i-1]:
                temp[i] = max(temp[i-1] + 1, temp[i])
            i +=1
        while 0 <= add:
            if ratings[add] > ratings[add+1]:
                temp[add] = max(temp[add+1] + 1, temp[add])
            add -=1
        return sum(temp)
    