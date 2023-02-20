class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
                
        def check(nums):
            
            temp = []
            distinct = []
            for i in range(3):
                cnt = 0
                for j in range(3):
                    cnt += nums[j][i]
                    distinct.append(nums[i][j])
                    
                temp.append(sum(nums[i]))
                temp.append(cnt)
        
            temp.append(nums[0][0] + nums[1][1] + nums[2][2])
            temp.append(nums[2][0] + nums[1][1] + nums[0][2])
            
            if len(distinct) != len(set(distinct)):
                return False
            
            for dist in distinct:
                if dist > 9 or dist < 1:
                    return False
            
            for l in range(1, len(temp)):
                if temp[l-1] != temp[l]:
                    return False
            return True
        
        n = len(grid)
        m = len(grid[0])
        
        if n < 3 or m < 3:
            return 0
        r = 0
        r_end = 3
        
        res = 0
        
        while r_end <= n:
            c = 0
            c_end = 3
        
            while c_end <= m:
                
                box = []
                for i in range(r, r_end):
                    rows = []
                    for j in range(c, c_end):
                        rows.append(grid[i][j])
                    box.append(rows)
                if check(box):
                    res += 1
                c_end += 1
                c += 1
            r += 1
            r_end += 1
            
        return res
                   
        
        """
        [[3,2,9,2,7],
         [6,1,8,4,2],
         [7,5,3,2,7],
         [2,9,4,9,6],
         [4,3,8,2,5]]
        """
                
                
                
                
                    