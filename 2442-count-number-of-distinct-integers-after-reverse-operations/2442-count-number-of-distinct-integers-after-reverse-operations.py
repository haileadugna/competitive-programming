class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n = len(nums[:])
        
        for i in range(n):
            temp = list(str(nums[i]))
            temp.reverse()
            nums.append(int("".join(temp)))
        res = len(set(nums))
        return res