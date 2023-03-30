class Solution:
    def hammingDistance(self, x: int, y: int) -> int:


        cnt = 0
        for j in range(32):

            if (x >> j) & 1 != (y >> j) & 1 or ((x >> j) & 1 != (y >> j) & 1) :
                cnt += 1

        return cnt