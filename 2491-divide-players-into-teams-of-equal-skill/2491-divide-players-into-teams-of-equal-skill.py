class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        if len(skill) == 2:
            return skill[0] * skill[1]
        left = 0
        right = len(skill) -1
        arr = []
        
        while left < right:
            if arr != []:
                if sum(arr[0]) == skill[left] + skill[right]:
                    arr.append([skill[left], skill[right]])
                    left += 1
                    right -= 1
                else:
                    return -1
            else:
                arr.append([skill[left], skill[right]])
                left += 1
                right -= 1
        res = 0
        for i in range(len(arr)):
            res += arr[i][0] * arr[i][1]
        return res
        