class Solution:
    def intToRoman(self, num: int) -> str:
        temp = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
        ans = ""
        while num >0:
            if num >= 1000:
                ans += temp[1000]
                num -=1000
            elif num >= 900:
                ans += temp[100] + temp[1000]
                num -= 900
            elif num >= 500:
                ans += temp[500]
                num -= 500
            elif num >= 400:
                ans += temp[100] + temp[500]
                num -= 400
            elif num >= 100:
                ans += temp[100]
                num -= 100
            elif num >= 90:
                ans += temp[10] + temp[100]
                num -= 90
            elif num >= 50:
                ans += temp[50]
                num -= 50
            elif num >= 40:
                ans += temp[10] + temp[50]
                num -= 40
            elif num >= 10:
                ans += temp[10]
                num -= 10
            elif num >= 9:
                ans += temp[1] + temp[10]
                num -= 9
            elif num >= 5:
                ans += temp[5]
                num -= 5
            elif num >= 4:
                ans += temp[1] + temp[5]
                num -= 4
            elif num >= 1:
                ans += temp[1]
                num -= 1
        return ans
            
            
