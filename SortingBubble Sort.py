def countSwaps(a):
    swaps=0
    for j in range(len(a)):
        for i in range(len(a)-1):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
                swaps+=1
    print('Array is sorted in',swaps,'swaps.')
    print('First Element:',a[0])
    print('Last Element:',a[-1])
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
