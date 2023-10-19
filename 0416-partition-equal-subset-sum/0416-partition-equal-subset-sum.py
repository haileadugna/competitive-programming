class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2 == 1:
            return False
        
        set_nums = set()
        set_nums.add(0)
        target = sum(nums)//2
        
        for i in range(len(nums) -2, -1, -1):
            # print(set_nums)
            temp = set()
            for t in set_nums:
                temp.add(t + nums[i])
                temp.add(t)
                # print('here', temp)
                
            set_nums = temp
            
        if target in set_nums:
            return True
        return False