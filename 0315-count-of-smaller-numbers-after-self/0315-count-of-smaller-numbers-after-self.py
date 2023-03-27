class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        temp = [i for i in range(len(nums))]
        res = [0] * (len(nums) + 1)
        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]
            mid = left + (right - left) // 2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)

            return merge(left_half, right_half)

        def merge(num1, num2):
            nonlocal res
 
            l, r = 0, 0
            num = []
            
            while l < len(num1) and r < len(num2):

                if nums[num2[r]] >= nums[num1[l]]:
                    num.append(num2[r])
                    r += 1
                    
                else:
                    num.append(num1[l])
                    res[num1[l]] += len(num2) - r
                    l += 1
            num.extend(num1[l:])
            num.extend(num2[r:])
            return num
            
        mergeSort(0, len(nums) -1, temp )
        res.pop()
        return res