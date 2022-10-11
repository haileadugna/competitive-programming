class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        l, m = 2**31,2**31
        for num in nums:
            if  num <= l:
                l = num
            elif num <= m:
                m = num
            else:
                return True
        return False
            
