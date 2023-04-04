class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        res = 0
        for i in range(len(nums)):
            prev = nums[i]
            for j in range(i, len(nums)):
                
                if nums[j] < k:
                    break
                gcd = math.gcd(prev, nums[j])
    
                if gcd < k:
                    break
                    
                elif gcd == k:
                    res += 1
                prev = gcd

        return res
  