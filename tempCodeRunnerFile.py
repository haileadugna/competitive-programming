# d= {'alice':19,'bob':23,'carl':47}
# print(list(d.items()))
# print(list(d.values()))
# print(list(d.keys()))
# t=[(k,v) for k,v in d.items()]
# print(t)
# temp=[]
# for k, v in d.items():
#     temp.append((k, v))
# print(temp)
# summ=list(zip(d.keys(),d.values()))
# print(summ)
# num=list(d.keys())
# nums=list(d.values())
# numm=nums+num
# print(numm)
# x = True
#         print(3) if x else print(5)
#         print([x for x in range(10)])

# class student:
#     def __init__(self, n, m ):
#         self.n=n
#         self.m=m
#     def addition(self,a,b):
#         s=a+b
#         return s
# s1= student(2,7)
# print(s1.sum(5,9))

arr = [1,1,3,4,2,4,-1,-4,-2,1,0]
a  = min(arr)
summ=[0]*(max(arr) + 1- a)

for j in range(len(arr)):
    summ[arr[j]- a]+=1

temp = []
for i in range(len(summ)):
    for k in range(summ[i]):
        temp.append(i + a)
       
print(temp)
