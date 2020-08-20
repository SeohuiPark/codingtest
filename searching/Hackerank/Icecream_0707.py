#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the icecreamParlor function below.
# 1 기준 인덱싱
# t아이스크림 구매 횟수 / m가진돈/ n아이스크림종류

#### 해쉬테이블로 풀기
## 가진돈에서 아이스크림 종류 가격 뺀 값이, 아이스크림 값 안에 있는지 체크... 천재적이당...

def icecreamParlor(m, arr):
    cost_dict = {}  ## key가 아이스크림 값 / value 가 아이스크림 인덱스
    for idx, icost in enumerate(arr):
        if m - icost in cost_dict:
            return [cost_dict[m - icost] + 1, str(idx + 1)]
        else:
            cost_dict[icost] = idx


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
