d= {'alice':19,'bob':23,'carl':47}
print(list(d.items()))
print(list(d.values()))
print(list(d.keys()))
t=[(k,v) for k,v in d.items()]
print(t)
temp=[]
for k, v in d.items():
    temp.append((k, v))
print(temp)
summ=list(zip(d.keys(),d.values()))
print(summ)
num=list(d.keys())
nums=list(d.values())
numm=nums+num
print(numm)