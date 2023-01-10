class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        val = (num + 3)/3
        res = []
        if val == int(val):
            res.append(int(val -2))
            res.append(int(val-1))
            res.append(int(val))
        return res