class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        count = {}
        ans = 0
        for num in deliciousness:
            for j in range(22):
                if 2**j - num in count:
                    ans += count[2**j - num]
                else:
                    continue
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        return ans%(10**9 +7)

            