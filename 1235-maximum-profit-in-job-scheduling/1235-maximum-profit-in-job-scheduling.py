class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        memo = [-1] * 50001

        def findMaxProfit(jobs, start, n, position):
            if position == n:
                return 0
            if memo[position] != -1:
                return memo[position]

            nextIndex = bisect.bisect_left(start, jobs[position][1])
            maxProfit = max(
                findMaxProfit(jobs, start, n, position + 1),
                jobs[position][2] + findMaxProfit(jobs, start, n, nextIndex),
            )

            memo[position] = maxProfit
            return maxProfit

        jobs = list(zip(startTime, endTime, profit))
        jobs.sort()

        for i in range(len(profit)):
            startTime[i] = jobs[i][0]

        return findMaxProfit(jobs, startTime, len(profit), 0)