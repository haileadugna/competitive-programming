class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        num1 = []
        changed.sort()
        c = Counter(changed)
        for i in range(len(changed)):
            if changed[i] == 0 and c[changed[i]] >=2:
                num1.append(0)
                c[changed[i]] -=2
            else:
                if changed[i]*2 in c and c[changed[i]] != 0 and changed[i] !=0 and c[changed[i]*2]!=0:
                    num1.append(changed[i])
                    c[changed[i]] -= 1
                    c[changed[i]*2] -= 1
        if len(num1) == len(changed)/2:
            return num1
        else:
            return []