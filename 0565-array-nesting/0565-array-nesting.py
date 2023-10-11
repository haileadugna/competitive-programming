class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        
        
        visited = set()
        res = []
        for i in range(len(nums)):
            if i not in visited:
                stack = [nums[i]]
                visit = set()
                while stack:
                    node = stack.pop()

                    if node not in visited:
                        visited.add(node)
                        visit.add(node)
                        stack.append(nums[node])
                        
            
                if len(visit) > len(res):
                    res = list(visit)
                    
                    
        return len(res)
                    
            