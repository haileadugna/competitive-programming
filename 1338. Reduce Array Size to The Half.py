class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dicts = {}
        n = len(arr)/2
        
        for i in arr:
            if i in dicts:
                dicts[i] += 1
            else:
                dicts[i] = 1
        temp = list(dicts.values())
        temp.sort()
        temp.reverse()
     
        num = 0
        output = 0
        for j in range(len(temp)):
            num += temp[j]
            output += 1
            if num >= n:
                break
        return output