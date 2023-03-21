class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        ans = set()  
        path = []
        def backtrack(idx):
            if idx == len(nums):
                if len(path) > 1:
                    ans.add(tuple(path))
                return
            
            # choose
            if not path:
                path.append(nums[idx])
                backtrack(idx + 1)
                path.pop()
            else:
                if path[-1] <= nums[idx]:
                    path.append(nums[idx])
                    backtrack(idx + 1)
                    path.pop()
            
            #not choose
            backtrack(idx + 1)
            
            
        backtrack(0)  
        return ans