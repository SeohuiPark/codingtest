#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the missingNumbers function below.
# 1두번 잃어버렸어도 한번 출력, 2출력은 오름차순, 3가장 큰수작은수 차이는 100보다작거나 같음

def missingNumbers(arr, brr):
    max_num = max(arr+brr)

    # make checklist with range 100!!!! (CONDITION3)
    check_list = [0 for _ in range(max_num-100, max_num+1)]


    # checklist 두번 채우기
    for a in arr:
        check_list[max_num-a] +=1
    for b in brr:
        check_list[max_num-b] -=1

    print(check_list)

    # checklist 꺼내는데 이때 매꿔지지 않은 친구들이 순차적으로 출력되도록
    # range(max_num-100, max_num+1) --> 순차적으로 값 확인 (오름차순 해결) (CONDITION2)
    # 모든 숫자를 한번씩 검토하고 2번 버려진 애들도 !=0 에 속하니까 return list 담김 (중복해결) (CONDITION1)
    return [y for y in range(max_num-100, max_num+1) if check_list[max_num-y] !=0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


#############