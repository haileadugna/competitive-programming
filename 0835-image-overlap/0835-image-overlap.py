class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        temp1 = []
        temp2 = []
        for i in range(len(img1)):
            for j in range(len(img1[0])):
                if img1[i][j] == 1:
                    temp1.append((i,j))
                if img2[i][j] == 1:
                    temp2.append((i,j))
        d = {}
        ans = 0
        for x, y in temp1:
            for a, b in temp2:
                tras = (a - x, b- y)
                if tras in d:
                    d[tras] += 1
                else:
                    d[tras] = 1
                ans = max(ans, d[tras])
                # print(d)
        return ans

