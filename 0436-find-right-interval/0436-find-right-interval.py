class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        temp = []
        for indx, [b,e] in enumerate(intervals):
            temp.append([b,e,indx])
        temp.sort()
        
        res = [-1]*len(intervals)
        
        vals = []
        for b, e, indx in temp:
            vals.append(b)
            
        for b, e, indx in temp:
            x = bisect.bisect_left(vals, e)

            if x != len(vals):
                res[indx] = temp[x][-1]
        return res