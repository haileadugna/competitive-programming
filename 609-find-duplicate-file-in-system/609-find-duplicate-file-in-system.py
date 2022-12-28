class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        res = []
        n = len(paths)
        dictt = defaultdict(list)
        for word in paths:
            temp = word.split(" ")
            m = len(temp)
            for  i in range(1, m):
                temp1 = temp[i].split("(")
                dictt[temp1[-1]].append(temp[0] + "/" + temp1[0])
        for key, item in dictt.items():
            if len(list(item)) > 1:
                res.append(item)
        return res