class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        nums1 = 0
        for i in range(len(num1)):
            if num1[i] == "+":
                numint1 = int(num1[:i])
                numcom1 = int(num1[i+1:-1])
        for j in range(len(num2)):
            if num2[j] == "+":
                numint2 = int(num2[:j])
                numcom2 = int(num2[j+1:-1])
        comp = numint1 * numcom2 + numint2 * numcom1
        integer = numint1 * numint2 - (numcom1 * numcom2)
        res = str(integer) + "+" + str(comp) + "i"
        return res