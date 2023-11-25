class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dictt = defaultdict(list)
        for link in cpdomains:
            temp = link.split(" ")
            temp1 = temp[1].split(".")
            ans = ""
            for i in range(len(temp1)-1,-1,-1):
                ans = "." + temp1[i]  + ans
                dictt[ans].append(temp[0])
        res = []
        for key, val in dictt.items():
            summ = 0

            for k in val:
                summ += int(k)
        
            temp2 = list(key)
            temp2 = "".join(temp2[1:])
            res.append(str(summ) + " " + temp2)
        return res
                