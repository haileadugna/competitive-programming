arr=[1,1,3,2,1]
summ=[]
nums=[]
output=[]
for i in range(max(arr)+1):
    summ.append(0)
for j in range(len(arr)):
    summ[arr[j]]+=1
for h in range(len(arr)):
    nums.append(h)
for k in range(len(summ)):
    for l in range(summ[k]):
        output.append(k)
print(output)
