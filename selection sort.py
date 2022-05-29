arr = [4, 1, 3, 9, 7]
i=5
for j in range(i-1):
    temp=j
    for k in range(j,i):
        if arr[temp]>arr[k]:
            temp=k
    templist=arr[j]
    arr[j]=arr[temp]
    arr[temp]=templist
print(arr)