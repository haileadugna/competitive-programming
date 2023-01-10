class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        temp = {}
        for l in range(len(boxes)):
            temp[l] = 0
        for i in range(len(boxes)):

            for j in range(i):
                if (boxes[j] == "1"):
                    temp[i] += abs(i-j)

            for j in range(i, len(boxes)):
                if (boxes[j] == "1"):
                    temp[i] += abs(i-j)

        res = list(temp.values())
        return res