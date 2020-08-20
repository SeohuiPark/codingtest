#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    b_arr, a_arr = [], arr.copy()
    while b_arr != a_arr:
        b_arr = a_arr.copy()
        pivot = b_arr[0]
        right_list, left_list, equal_list = [],[],[]
        for num in b_arr:
            if num > pivot: right_list.append(num)
            elif num < pivot:left_list.append(num)
            else:equal_list.append(num)
        a_arr = left_list + equal_list+ right_list
        # print(b_arr,"-->", a_arr)

    return a_arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
