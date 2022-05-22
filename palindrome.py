class Solution:
    def isPalindrome(self, x: int) -> bool:
        count= len(str(x))
        org = x
        temp =0
        while count>0:
            num = x%10
            x = x//10
            temp += num*10**(count-1) 
            count -=1
        return temp == org