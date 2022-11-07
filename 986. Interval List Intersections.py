class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        l, r = 0, 0
        ans = []
        while l < len(firstList) and r < len(secondList):
            if firstList[l][0] < secondList[r][0]:
                if firstList[l][1] >= secondList[r][0]:
                    if firstList[l][1] > secondList[r][1]:
                        ans.append(secondList[r])
                        r += 1
                    else:
                        ans.append([secondList[r][0], firstList[l][1]])
                        l += 1
                else:
                    l += 1
            else:
                if firstList[l][0] <= secondList[r][1]:
                    if firstList[l][1] < secondList[r][1]:
                        ans.append(firstList[l])
                        l += 1
                    else:
                        ans.append([firstList[l][0], secondList[r][1]])
                        r += 1
                else:
                    r += 1
        return ans