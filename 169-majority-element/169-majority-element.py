class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # def majorityElement(nums):
    # base case: if the input array has length 1, the majority element is the only element
        if len(nums) == 1:
            return nums[0]

        # divide the input array into two halves
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        # recursively find the majority element in each half
        majority_left = self.majorityElement(left)
        majority_right = self.majorityElement(right)

        # if the majority element in the first half is the same as the majority element in the second half, return that element
        if majority_left == majority_right:
            return majority_left

        # if they are different, count the number of occurrences of each element and return the element with the most occurrences
        count_left = sum(1 for i in nums if i == majority_left)
        count_right = sum(1 for i in nums if i == majority_right)
        if count_left > count_right:
            return majority_left
        else:
            return majority_right