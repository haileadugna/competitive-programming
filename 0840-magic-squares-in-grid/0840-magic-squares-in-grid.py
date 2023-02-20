class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        # Define a function check that will check if the input list of numbers forms a magic square or not
        def check(nums):
            # Initialize variables temp, distinct
            temp = []
            distinct = []
            # Iterate over the rows and columns of the 3x3 grid
            for i in range(3):
                cnt = 0
                for j in range(3):
                    # Sum up the elements of the column
                    cnt += nums[j][i]
                    # Add each element to the distinct list
                    distinct.append(nums[i][j])
                # Add the sum of each row and column to the temp list
                temp.append(sum(nums[i]))
                temp.append(cnt)

            # Calculate the sum of the diagonal elements and add it to the temp list
            temp.append(nums[0][0] + nums[1][1] + nums[2][2])
            temp.append(nums[2][0] + nums[1][1] + nums[0][2])

            # If there are any duplicate elements in the distinct list, return False
            if len(distinct) != len(set(distinct)):
                return False

            # If any element is outside the range of 1-9, return False
            for dist in distinct:
                if dist > 9 or dist < 1:
                    return False

            # If all the sums are equal to each other, return True
            for l in range(1, len(temp)):
                if temp[l-1] != temp[l]:
                    return False
            return True

        # Get the dimensions of the grid
        n = len(grid)
        m = len(grid[0])

        # If the dimensions are less than 3x3, return 0
        if n < 3 or m < 3:
            return 0

        # Initialize variables r, r_end, c, c_end, and res
        r = 0
        r_end = 3
        res = 0

        # Use two while loops to iterate over all possible 3x3 sub-grids in the larger grid
        while r_end <= n:
            c = 0
            c_end = 3

            while c_end <= m:
                # Extract the sub-grid using nested loops and check if it forms a magic square
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

        # Return the number of magic squares found
        return res
                   
        
        """
        [[3,2,9,2,7],
         [6,1,8,4,2],
         [7,5,3,2,7],
         [2,9,4,9,6],
         [4,3,8,2,5]]
        """
                
                
                
                
                    