class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        s, e = 0, len(nums)-1
        tmp = []
        while s <= e:
            if abs(nums[s]) > abs(nums[e]):
                tmp.append(nums[s]**2)
                s += 1
            else:
                tmp.append(nums[e]**2)
                e -= 1
        tmp.reverse()
        return tmp