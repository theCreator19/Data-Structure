# 2D Array - DS
# HackerRank Problem Solved using Python.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    max=-1000000
    for i in range(4):
        for j in range(4):
            a=arr[i][j]
            b=arr[i][j+1]
            c=arr[i][j+2]
            d=arr[i+1][j+1]
            e=arr[i+2][j]
            f=arr[i+2][j+1]
            g=arr[i+2][j+2]
            
            if(max<a+b+c+d+e+f+g):
                max=a+b+c+d+e+f+g
        
    return max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
