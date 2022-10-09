class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        ans = [0] * (len(num1) + len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                temp = int(num1[i]) * int(num2[j])
                ans[i +j] += temp
                ans[i +j + 1] += ans[i + j]// 10
                ans[i +j] = ans[i + j]%10
        ans, tmp = ans[::-1], 0
        while tmp < len(ans) and ans[tmp] ==0:
            tmp += 1
        ans = map(str, ans[tmp:])
        return "".join(ans)