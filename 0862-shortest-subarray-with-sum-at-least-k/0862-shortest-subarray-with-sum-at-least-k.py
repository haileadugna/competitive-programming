class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        summ = 0
        stack = deque()
        l = 0
        nums.insert(0, 0)
        res = len(nums) + 1
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            
            if nums[i] < 0:
                nums[i] = 0
        nums = nums[1:]
    
        for i in range(len(nums)):
            if nums[i] >= k:
                while stack and nums[i] - nums[stack[0]] >= k:
                    l = 1 + stack.popleft()  
                res = min(res, i - l + 1 ) 
                
            while stack and nums[stack[-1]] > nums[i] and nums[i] > 0:
                stack.pop()
            stack.append(i)
            
        if res >= len(nums) + 1:
            return -1
        
        return res