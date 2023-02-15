class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        temp = (num[-1] + k)//10
        num[-1] = (num[-1] +k)%10
        i = len(num) -2
        while i >= 0 and temp > 0:
            num[i] += temp
            temp = num[i]//10
            num[i] %= 10
            i -=1
        while temp > 0:
            num[:0] = [temp%10]
            temp //= 10
        return num