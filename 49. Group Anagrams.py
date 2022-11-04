class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = defaultdict(list)
        for s in strs:
            key = "".join(sorted(list(s)))
            temp[key].append(s)
        ans = []
        for l in temp.values():
            ans.append(l)
        return ans
        # ans = []
        # cur = []
        # for i in range(len(strs)):
        #     ans1 = []
        #     temp = Counter(list(strs[i]))
        #     # ans1.append(strs[i])
        #     for j in range(len(strs)):
        #         if j in cur :
        #             continue
        #         else:
        #             temp1 = Counter(list(strs[j]))
        #             if temp == temp1:
        #                 ans1.append(strs[j])
        #                 cur.append(j)
        #             else:
        #                 continue
        #     if ans1 == []:
        #         continue
        #     else:
        #         ans.append(ans1)
        #         ans1 = []
        # return ans
