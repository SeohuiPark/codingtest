#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the balancedSums function below.
def balancedSums(arr):
    # 1. initialize index
    start_idx, end_idx = 0, len(arr) - 1
    mid_idx = (start_idx + end_idx) // 2

    # 2. initalize list
    left_list, right_list = arr[: mid_idx], arr[mid_idx + 1:]

    # 3. loop - until list of sum is same

    while sum(left_list) != sum(right_list):
        # +) backup before index
        b_st, b_mi, b_en = start_idx, mid_idx, end_idx

        # case1. 인덱스가 양 끝인 경우
        if mid_idx == 0: left_list = [0]
        if mid_idx == len(arr) - 1:
            right_list = [0]

        # case2. 인덱스가 양 끝이 아닌 경우 (binary search)
        else:
            if sum(left_list) > sum(right_list):
                end_idx = mid_idx
            else:
                start_idx = mid_idx

            # +) backup after index
            a_st, a_mi, a_en = start_idx, mid_idx, end_idx

        # 4. check index  changed
        if (b_st == a_st) and (b_mi == a_mi) and (b_en == a_en):
            break  # 인덱스 안바뀌면, 더이상 찾는 수가 없는거임.(끝내기)
        else:  # 인덱스 바뀌었으면, 다시 리스트 셋팅  --> 만약 여기서 두 리스트 합 같으면 반복문 멈춤.
            mid_idx = (start_idx + end_idx) // 2
            left_list, right_list = arr[: mid_idx], arr[mid_idx + 1:]

    # 5. final
    if sum(left_list) != sum(right_list):
        result = "NO"
    else:
        result = "YES"
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
