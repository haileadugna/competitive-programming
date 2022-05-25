class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        temp=[]
        ans=[]
        for point in points:
            nums = (point[0])**2+(point[1])**2
            temp.append([nums,point])      
        temp.sort()
        for j in range(k):
            ans.append(temp[j][1])         
        return ans