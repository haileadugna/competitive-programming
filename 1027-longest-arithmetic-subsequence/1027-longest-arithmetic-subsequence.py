class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [{} for _ in range(n)]
        res = 0

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    dp[i][diff] = 2
                res = max(res, dp[i][diff])
        # print(dp)
        return res
        
        #the brute force solution n^4 time complicity

#         dictt = defaultdict(list)
        
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
                
#                 dictt[nums[i] - nums[j]].append((i, j))
                
#         # print(dictt)
#         res = 0
#         for key in list(dictt.keys()):
#             cnt = 1
#             alist = dictt[key]
#             # ans = []
#             for i in range(len(alist) - 1):
#                 temp = 1
#                 val = i
#                 for j in range(i+ 1, len(alist)):
#                     if alist[val][1] == alist[j][0]:
#                         temp += 1
#                         val = j
#                         # ans.append((alist[i], alist[i + 1]))
                
#                 cnt = max(cnt, temp)
#             # print(ans)
#             res = max(cnt, res)
#         return res + 1
                