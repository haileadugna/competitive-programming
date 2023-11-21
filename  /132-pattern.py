class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        stack = []
        pre = min(nums)
        
        for i in range(len(nums)-1, -1, -1):
            
            if stack and stack[-1] < pre:
                return True
            while stack and stack[-1] < nums[i]:
                pre = stack.pop()
                
            stack.append(nums[i])
        if stack and stack[-1] < pre:
            return True
            
        return False
                
