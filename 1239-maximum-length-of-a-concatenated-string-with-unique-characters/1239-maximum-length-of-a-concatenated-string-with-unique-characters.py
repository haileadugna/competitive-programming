class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        res = 0
        def backtrack(i, arr, path):
            nonlocal res
            if len("".join(path)) == len(set("".join(path))):
                res = max(res, len("".join(path)))

            for j in range(i+1, len(arr)):
                path.append(arr[j])
                backtrack(j,arr, path)
                path.pop()
          
        backtrack(-1, arr, [""])
        return res