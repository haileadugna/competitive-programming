class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        ans = 0
        for i in range(1,len(salary)-1):
            ans += salary[i]
        ans = ans/(len(salary)-2)
        return ans