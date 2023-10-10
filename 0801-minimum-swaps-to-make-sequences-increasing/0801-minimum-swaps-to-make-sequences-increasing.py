class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        
        @cache
        def dp(cur_1, cur_2, prev1, prev2):
            
            if cur_1 < 0 and cur_2 < 0:
                return 0
            
            ans = float('inf')
            
            if nums1[cur_1] < prev1 and nums2[cur_2] < prev2:
                
                val = dp(cur_1 -1, cur_2 -1,  nums1[cur_1], nums2[cur_2])
                ans = min(val, ans)
                
            if nums2[cur_1] < prev1 and nums1[cur_2] < prev2:
                val = dp(cur_1 -1, cur_2 -1,  nums2[cur_1], nums1[cur_2]) + 1
                ans = min(val, ans)
                
            return ans
                
                
        return dp(len(nums1)-1, len(nums2)-1, float('inf'), float('inf'))