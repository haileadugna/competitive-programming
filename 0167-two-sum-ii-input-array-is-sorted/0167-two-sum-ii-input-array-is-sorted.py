class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize the left pointer at the start of the list and the right pointer at the end of the list
        left = 0
        right = len(numbers) - 1

        # Use a while loop to iterate until the left pointer is equal to or greater than the right pointer
        while left < right:
            # Calculate the sum of the elements at the left and right pointers
            summ = numbers[left] + numbers[right]
            # If the sum is equal to the target, return the indices of the elements
            if summ == target:
                return [left + 1, right + 1]
            # If the sum is greater than the target, decrement the right pointer
            elif summ > target:
                right -= 1
            # If the sum is less than the target, increment the left pointer
            else:
                left += 1