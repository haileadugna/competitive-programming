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

# arr = [1,1,3,4,2,4,-1,-4,-2,1,0]
# a  = min(arr)
# summ=[0]*(max(arr) + 1- a)

# for j in range(len(arr)):
#     summ[arr[j]- a]+=1

# temp = []
# for i in range(len(summ)):
#     for k in range(summ[i]):
#         temp.append(i + a)
       
# print(temp)

# arr =  [4, 1, 3, 9, 7]
# n = len(arr)
# summ = []
# for i in range(n-1):
#     temp = i
#     for k in range(i+1, n):
#         if arr[temp] > arr[k]:
#             temp = k
#     if i != temp:
#         a= arr[i]
#         arr[i]=arr[temp]
#         arr[temp] = a
# print(arr)
# arr = [1,2,3,4,5,6,7,4]
# n = len(arr)
# e= arr[-1]

# for i in range(n-2,-1,-1):
#     if arr[i]<e:
#         arr[i+1]= e
#         temp=list(map(str,arr))
#         out=' '.join(temp)
#         print(out)
#         break
#     else:
#         arr[i+1]=arr[i]
#         temp=list(map(str,arr))
#         out=' '.join(temp)
#         print(out)
# else:
#     arr[0]=e
#     temp=list(map(str,arr))
#     out=' '.join(temp)
#     print(out)

arr = [5,3,2,4,6,3,4]
n= len(arr)
for i in range(n-1):
    temp = i
    for k in range(i+1, n):
        if arr[temp] > arr[k]:
            temp = k
    if i != temp:
        a= arr[i]
        arr[i]=arr[temp]
        arr[temp] = a
    print(arr)