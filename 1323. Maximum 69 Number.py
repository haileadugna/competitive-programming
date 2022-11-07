class Solution:
    def maximum69Number (self, num: int) -> int:
        num = list(str(num))
        i = 0
        print(num)
        while i < len(num) and num[i] == "9" :
            i += 1
        if i < len(num):
            num[i] = "9"
        return int("".join(num))
