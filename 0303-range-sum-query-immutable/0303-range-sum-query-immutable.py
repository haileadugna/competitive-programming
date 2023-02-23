class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        temp = 0
        for i in range(len(nums)):
            temp += self.nums[i]
            self.nums[i] = temp
        print(nums)
        

    def sumRange(self, left: int, right: int) -> int:
        
        if left > 0:
            return self.nums[right] - self.nums[left - 1]
        return self.nums[right]
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)