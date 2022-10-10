class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # ans = ""
        # for i in range(len(num)):
        #     ans += str(num[i])
        # ans = int(ans) + k
        # temp = []
        # count = len(str(ans))-1
        # while count >= 0:
        #     temp.append(ans//10**count)
        #     ans = ans % 10**count
        #     count -= 1
        # return temp
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

