def countSwaps(a):
    swaps = 0
    def countswap(a, swaps):
        for i in range(1, len(a)):
            if a[i]<a[i-1]:
                a[i],a[i-1] = a[i-1], a[i]
                swaps+=1
            return countswap(a, swaps)
        else:
            return swaps
    print("Array is sorted in", countswap(a, swaps), "swaps")
    print("First Element: ",a[0])
    print("Last Element: ", a[-1])