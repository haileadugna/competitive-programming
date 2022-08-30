class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        palindrome  = list(palindrome)
        for j in range(len(palindrome)//2):
            if palindrome[j] != "a":
                palindrome[j] = "a"
                return "".join(palindrome)
        palindrome[-1] = "b"
        return "".join(palindrome)