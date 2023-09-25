class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        nums = []
        for i in range(len(scores)):
            nums.append([ages[i], scores[i]])
            
        nums.sort()
        
        print(nums)
        dp = defaultdict(int)
        res = 0
        for i in range(len(nums)-1, -1,-1):
            prev = nums[i][1]
            
            if prev in dp and prev > max(dp.keys()):
                dp[prev] += prev
            else:
                temp = -1
                t_max = float("-inf")
                # print(list(dp.keys()))
                for i in list(dp.keys()):
                    if i < prev:
                        continue
                    else:
                        t_max = max(t_max, dp[i])
                        temp = 1
                        
                if temp != -1:
                    dp[prev] = t_max + prev
                else:
                    dp[prev] += prev
                        
                # print(dp, t_max)
            
                
        # print(dp)   
            
            # res = max(res, cur_sum)
            
        return max(dp.values())
                