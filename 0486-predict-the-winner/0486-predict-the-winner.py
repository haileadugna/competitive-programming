class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        if len(nums) == 1:
            return True
        def winner(left, right):
 
            if left > right:
                return 0
            if left == right:
                return nums[left]
            
            tempmax1 = nums[left] + min(winner(left + 2, right), winner(left + 1, right-1))

            tempmax2 = nums[right] + min(winner(left + 1, right - 1), winner(left, right - 2))

            return max( tempmax1, tempmax2 )
                    
        max_score = winner(0, len(nums) - 1)

        return max_score >= sum(nums)/2
                    
                
            
            