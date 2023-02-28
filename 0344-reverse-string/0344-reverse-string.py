class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverses(s, left, right):
            if left >= right:
                return s
            else:
                s[left] , s[right] = s[right], s[left]
                return reverses(s, left + 1, right -1)
            
        return reverses(s, 0, len(s) -1)
        