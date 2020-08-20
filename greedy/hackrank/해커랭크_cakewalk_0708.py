#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marcsCakewalk function below.
def marcsCakewalk(calorie):
    sorted_calorie = reversed(sorted(calorie))
    allcal_list = []
    for idx, cal in enumerate(sorted_calorie):
        allcal_list.append((2**idx)*cal)

    return (sum(allcal_list))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    calorie = list(map(int, input().rstrip().split()))
    result = marcsCakewalk(calorie)
    fptr.write(str(result) + '\n')

    fptr.close()
