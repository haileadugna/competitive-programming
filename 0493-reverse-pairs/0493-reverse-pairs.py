class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        res = 0
        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]
            mid = left + (right - left) // 2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)

            return merge(left_half, right_half)

        def merge(num1, num2):
            nonlocal res
            s, e = 0, 0
            n = len(num1)
            while s < len(num1) and e < len(num2):
                if num2[e] < num1[s]:
                    if num2[e] * 2 < num1[s]:
                        res += (n - s)
                        e +=1
                    else:
                        s += 1
                    
                else:
                    if num2[e] * 2 < num1[s]:
                        res += (n - s)
                        e +=1
                    else:
                        s += 1
                    
            l, r = 0, 0
            nums = []
            
            while l < len(num1) and r < len(num2):
                # print(num1, "her", num2)
                if num2[r] < num1[l]:
                    nums.append(num2[r])
                    r += 1
                    
                else:
                    nums.append(num1[l])
                    l += 1
            nums.extend(num1[l:])
            nums.extend(num2[r:])
            return nums
            
        mergeSort(0, len(nums) -1, nums )
        return res
    
    
    
    