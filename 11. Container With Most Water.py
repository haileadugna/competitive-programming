class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        ans = 0
        while l < r:
            temp = min(height[l], height[r])
            ans = max(ans, temp*(r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans