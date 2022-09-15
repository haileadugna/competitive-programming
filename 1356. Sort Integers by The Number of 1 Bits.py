class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        nums = {}
        arr.sort()
        ans = []
        for i in arr:
            count = bin(i).count("1")
            if count not in nums:
                nums[count] =[i]
            else:
                nums[count].append(i)
        for j in sorted(nums.keys()):
            ans.extend(nums[j])
        return ans