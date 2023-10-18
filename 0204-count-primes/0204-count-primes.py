class Solution:
    def countPrimes(self, n: int) -> int:
        
        
        nums = [0] * (n)
        
        for i in range(2, n//2 + 1):
            
            if i*i > n:
                break
                
            else:
                if nums[i] ==1:
                    continue
                    
                else:
                    for j in range(i, n ):
                        
                        if j*i < n :
                            nums[j*i] = 1
                            
                        else:
                            break
          
        # print(nums)
        count = 0
        for i in range(2, len(nums)):
            if nums[i] == 0:
                count += 1
        
        return count