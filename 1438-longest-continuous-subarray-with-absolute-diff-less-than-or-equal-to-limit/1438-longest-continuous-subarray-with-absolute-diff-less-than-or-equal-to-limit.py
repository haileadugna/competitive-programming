class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        increase = deque()
        decrease = deque()
        res = 1
        left, right = 0, 1
        increase.append(0)
        decrease.append(0)
        
        while right < len(nums):
            while increase and nums[increase[-1]] > nums[right]:
                increase.pop()
            increase.append(right)
            while decrease and nums[decrease[-1]] < nums[right]:
                decrease.pop()
            decrease.append(right)
            if nums[decrease[0]] - nums[increase[0]] > limit:
                left += 1
                while increase and increase[0] < left:
                    increase.popleft()
                while decrease and decrease[0] < left:
                    decrease.popleft()
                    
            right += 1
            res = max(res, right - left)

        return res
            