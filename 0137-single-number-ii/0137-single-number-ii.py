class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        # return reduce(lambda a, b, c: (a&b) ^ c, nums)
        c = 2
        while c < len(nums):
            prev = nums[c-2] & nums[c-1] ^ nums[c]
            if prev == 0:
                c += 3
            else:
                temp  = nums[c-2: c+1]
                return temp[0]
                break

        return nums[-1]