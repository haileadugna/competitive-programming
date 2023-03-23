class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        dictt = Counter(nums)
        for i in range(1, max(nums) + 3):
            if i not in dictt:
                return i
        return 1
     