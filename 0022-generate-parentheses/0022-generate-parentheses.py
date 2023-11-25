class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def parent(left, right, stack, cand):
            if left == right == 0:
                ans.append(cand)
                return
            if left > 0:
                parent(left -1, right, stack + 1, cand + "(")
            if right > 0 and stack > 0 :
                parent(left, right - 1, stack - 1, cand + ")")
        parent(n, n, 0, "")
        return ans