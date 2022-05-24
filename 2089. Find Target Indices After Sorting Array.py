nums=[1,2,5,2,3]
target=6
nums.sort()
output=[]
for i in range(len(nums)):
    if nums[i]==target:
        output.append(i)

print(output)