class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # nums.sort()
        tmp = Counter(nums)
        for i in range(1, len(nums)+1):
            if i not in tmp:
                count = i
            elif tmp[i] == 2:
                tmp2 = i
        return [tmp2, count]
            



