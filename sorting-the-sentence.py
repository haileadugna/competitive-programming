class Solution:
    def sortSentence(self, s: str) -> str:
        output=[]
        new=[]
        list1=list(s.split(" "))
        for i in range(len(list1)):
            num=int(list1[i][-1])
            word=(list1[i])[:-1]
            temp=[num,word]
            output.append(temp)
        output.sort()
        for j in range(len(output)):
            new.append(output[j][1])
        sentence=' '.join(new)
        return sentence