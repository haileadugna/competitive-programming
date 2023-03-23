class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        def quickSort(left, right, arr):
            nonlocal n, k
            read = left + 1
            write = left + 1

            while read < right+1 :
                if arr[left] >= arr[read]:
                    arr[write], arr[read] = arr[read], arr[write]
                    write += 1
                read += 1

            arr[left], arr[write - 1] = arr[write - 1], arr[left]

            if n - (write -1) > k:
                quickSort(write, right, arr)
            elif n - (write -1) < k:
                quickSort(left, write - 2, arr)

        quickSort(0, len(nums) - 1, nums)

        return nums[n - k]