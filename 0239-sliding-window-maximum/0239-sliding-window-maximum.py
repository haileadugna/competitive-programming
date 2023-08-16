class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        que = deque()
        ans = []
        
        for i in range(n):
            
            while que and nums[que[-1]] < nums[i]:
                que.pop()
                
            que.append(i)
            
            if i >= k-1:
                temp = bisect_left(que, i - k +1)
                # print(temp, i - k +1, que)
                ans.append(nums[que[temp]])
#                 for j in range(len(que) -1, -1, -1):
                    
                    
                    
#                     if j == 0 and i - que[j] <= k -1:
#                         ans.append(nums[que[j]])
#                         break
#                     elif i - que[j] == k-1:
#                         ans.append(nums[que[j]])
#                         break

#                     elif i - que[j] > k -1:
#                         ans.append(nums[que[j + 1]])
#                         break
            # print(que)        
        return ans
                
                
            