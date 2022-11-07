class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        tot = 0
        temp = {0:1}
        ans =0
        for j in nums:
            tot += j
            diff = tot -k

            ans += temp.get(diff, 0)
            temp[tot] = 1 + temp.get(tot,0)
        return ans