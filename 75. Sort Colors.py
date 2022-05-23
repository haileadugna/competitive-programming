nums =[2,0,2,1,1,0]
sum=[]
temp=[]
for i in range(3):
    sum.append(0)
for j in range(len(nums)):
    sum[nums[j]]+=1
for k in range(3):
    for l in range(sum[k]):
        temp.append(k)
print("[{}]".format(",".join(map(repr, temp))))
