class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        res = 0
        def backtrack(arr, path):
            nonlocal res
            if len("".join(path)) == len(set("".join(path))):
                res = max(res, len("".join(path)))

            for i in range(len(arr)):
                path.append(arr[i])
                backtrack(arr[i + 1:], path)
                path.pop()
          
        backtrack(arr, [""])
        return res