#!/bin/python3

import math
import os
import random
import re
import sys

'''
stack --> 먼저들어온 친구의 반대가 맨 나중에 나가는 {}
짝이 없는 친구들은 없다. 
open 친구 들어올때마다 open stack 에 저장 
close 친구들어오면 open stack 에 짝궁 있는지 체크 
있으면 open stack 에 짝궁 pop
없으면 return NO
끝까지 문제 없이 다 돌면 YES

'''


# Complete the isBalanced function below.
def isBalanced(s):
    s = list(s)
    open_values = ["{", "[", "("]
    close_values = ["}", "]", ")"]

    open_stack = []
    result = True

    for one_s in s:
        if one_s in open_values:
            open_stack.append(one_s)
        elif one_s in close_values:
            close_val_idx = close_values.index(one_s)
            close_partner = open_values[close_val_idx]
            if len(open_stack) == 0 or (close_partner != open_stack[-1]):
                result = False
                break
            elif close_partner == open_stack[-1]:
                open_stack.pop()
        print(open_stack)
    if len(open_stack) == 0 and result:
        return ("YES")
    else:
        return ("NO")


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
