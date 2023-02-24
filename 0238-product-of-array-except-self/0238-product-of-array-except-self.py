class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = []
        temp = 1
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                tmp = i
                count += 1
            else:
                temp *= nums[i]
        if count > 1:
            return [0]* len(nums)
        elif count == 1:
            for i in range(len(nums)):
                if i != tmp:
                    ans.append(0)
                else:
                    ans.append(temp)
        else:
            for j in range(len(nums)):
                ans.append(temp//nums[j])
        return ans