nums=[3,30,34,5,9]
temp=[]
ans=""
for i in nums:
    temp.append(str(i))
temp.sort()
temp.reverse()
for k in range(len(temp)):
    for j in range(len(temp)-1):
        start = temp[j] + temp[j+1]
        end = temp[j+1]+temp[j]
        if end>start:
            temp[j],temp[j+1]=temp[j+1],temp[j]
        else:
            ans += temp[j]
print(ans)
