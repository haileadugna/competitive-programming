#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    e= arr[-1]
    for i in range(n-2,-1,-1):
        if arr[i]<e:
            arr[i+1]= e
            temp=list(map(str,arr))
            out=' '.join(temp)
            print(out)
            break
        else:
            arr[i+1]=arr[i]
            temp=list(map(str,arr))
            out=' '.join(temp)
            print(out)
    else:
        arr[0]=e
        temp=list(map(str,arr))
        out=' '.join(temp)
        print(out)
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
