class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        s, e = 0, len(mat[0])-1
        ans = {}
        tmp =0
        for arr in mat:
            while s <= e:
                mid = (s+e)//2
                if arr[mid] ==0 :
                    e = mid-1
                else:
                    s = mid +1
            ans[tmp] = s
            tmp += 1
            s, e = 0, len(mat[0])-1
        temp = []
        for key, val in ans.items():
            temp.append([val, key])
        temp.sort()
        finalans = []
        for i in range(k):
            finalans.append(temp[i][1])
        return finalans
            
            