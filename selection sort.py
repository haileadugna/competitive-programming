#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        for j in range(i):
            temp = arr[j]
    def selectionSort(self, arr,n):
        #code here
        for i in range(n-1):
            temp = i
            for k in range(i+1, n):
                if arr[temp] > arr[k]:
                    temp = k
            if i != temp:
                a= arr[i]
                arr[i]=arr[temp]
                arr[temp] = a
        return arr
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends