class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # tmp = {}
        # for i in range(len(nums)):
        #     tmp[nums[i]] = i
        # print(tmp)
        tmp = nums[:]
        ans = []
        nums.sort()
        start, end = 0, len(nums)-1
        while start <= end:
            if nums[start] + nums[end] == target :
                ans.append(nums[start])
                ans.append(nums[end])
                break
            elif nums[start] + nums[end] > target :
                end -= 1
            else:
                start += 1
        temp = []
        for i in range(len(tmp)):
            if tmp[i] == ans[0] or tmp[i] == ans[1]:
                temp.append(i)
        return temp