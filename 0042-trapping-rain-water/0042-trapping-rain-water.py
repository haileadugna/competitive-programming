class Solution:
    def trap(self, height: List[int]) -> int:
        
        if len(height) == 0:
            return 0
        
        ans = 0
        left_max = [-1 for i in range(len(height))]
        right_max = [-1 for i in range(len(height))]
        left_max[0] = height[0]
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i-1], height[i])
            
            
        right_max[-1] = height[-1]
        for i in range(len(height) -2, -1, -1):
            right_max[i] = max(height[i], right_max[i+1])
            
        # print(left_max)
        # print(right_max)
        for i in range(1, len(height) -1):
            ans += min(left_max[i], right_max[i]) - height[i]
            
        return ans