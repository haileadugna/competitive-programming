class Solution:
    def jump(self, nums: List[int]) -> int:
        # If the input list only contains one element, return 0
        if len(nums) == 1:
            return 0
        # Initialize the starting position as 0 and the jump count as 1
        l = 0
        count = 1
        # Loop until the end of the input list is reached
        while l < len(nums)-1:
            # If the current position can reach the end of the input list, return the jump count
            if nums[l] + l >= len(nums) -1:
                return count
            # Store the maximum reachable distance from the current position
            r = nums[l]
            # If the current position can't move, break the loop
            if r == 0:
                break
            # Initialize the next jump position, maximum jump length, and the maximum reachable distance
            jumb = 0
            temp = 0
            # Loop through the reachable positions from the current position
            for i in range(l+1, r+l+1):
                # If the current position has a larger jump length or a further reachable distance, update the next jump position
                if nums[i] > jumb or i + nums[i] > temp:
                    j = i
                    jumb = nums[i]
                    temp = i + nums[i]
            # Update the current position as the next jump position
            l = j
            jumb = 0
            # Increment the jump count by 1
            count += 1