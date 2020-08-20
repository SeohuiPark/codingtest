#!/bin/python3

import math
import os
import random
import re
import sys

'''
# 거의 정렬에 가까운 어레이 
# 낮은 인덱스 값들 (0~3)을 테스트 하며, arr[4] 보다 낮은 곳에 도달 
## 비교값보다 낮지 않으면, 낮은  값(3)을 현재의 값(4) 으로 덮어씌움 12435 --> 12445
## 맞으면 그대로 출력 12345

인덱스 뒤에서부터
for 문 돌고 / key3 값보다 arr[i]5 가 크면 
12435로 만들고 3에 5 덮어씌우기
'''


# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    key = arr[-1]
    arr_nokey = arr[:-1]

    for i in reversed(range(0, len(arr) - 1)):  # 3,2,1,
        if arr_nokey[i] > key:
            result = arr_nokey[:i] + [arr_nokey[i]] + arr_nokey[i:]
            print(' '.join(map(str, result)))

            if (i == 0) and (key not in result):
                result = [key] + arr_nokey[i:]
                print(' '.join(map(str, result)))
                break

        else:
            result = arr_nokey[:i + 1] + [key] + arr_nokey[i + 1:]
            print(' '.join(map(str, result)))
            break

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
