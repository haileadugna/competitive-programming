class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack=[intervals[0]]
        for i in range(1,len(intervals)):
            if stack[-1][1] >= intervals[i][0]:
                stack[-1][1] = max(intervals[i][1] , stack[-1][1])
            else:
                stack.append(intervals[i])
        return stack