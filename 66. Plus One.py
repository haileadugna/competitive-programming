class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        if digits[-1] < 9:
            ans = digits.pop() + 1
            digits.append(ans)
            return digits
        else:
            temp = []
            count = 0
            for i in range(n-1, -1, -1):
                if digits != [] and digits[i] == 9:
                    count += 1
                    digits.pop()
                else:
                    break
            if digits == []:
                digits.append(1)
            else:
                ans = digits.pop() + 1
                digits.append(ans)
            for i in range(count):
                digits.append(0)
            return digits
