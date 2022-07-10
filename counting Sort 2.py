arr=[1,1,3,2,1,3,2,2,2,1,1,3,3,3,2,1,2,3,2,1,2,3,2,1,2]
summ=[0]* (max(arr)+1)
output=[]
for j in range(len(arr)):
    summ[arr[j]]+=1
print(summ)
for k in range(len(summ)):
    for l in range(summ[k]):
        output.append(k)
print(output)
