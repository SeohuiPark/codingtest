#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    print(contests)

    im_luck = sorted([i[0] for i in contests if i[1] == 1])
    un_lunk = sorted([i[0] for i in contests if i[1] == 0])

    if k >= len(im_luck): # 져도 되는 횟수가 중요 경기 횟수보다 많으면
        print("Nominus")
        result = sum(im_luck+un_lunk) # 다졌다고 생각하쟝

    elif k < len(im_luck): # 져도 되는 횟수가 경기 횟수보다 작으면 3//5
        print("Yesminus")
        win_time = len(im_luck) - k #2번은 반드시 이겨줘야함
        win_luck = im_luck[:win_time] #제일 행운 적은 2번 경기 이겨주자규
        lose_luck = im_luck[win_time:] #나머지 경기는 진경기
        result = sum(lose_luck+un_lunk) - sum(win_luck)
        print("win_luck",win_luck)

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
