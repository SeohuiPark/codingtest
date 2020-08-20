#!/bin/python3

import math
import os
import random
import re
import sys
import time
start = time.time()

# Complete the gridChallenge function below.
def gridChallenge(grid):
    sorted_2dlist= ([sorted(i) for i in grid])
    for r in range(len(sorted_2dlist)-1): #0,1,2,3
        for c in range(len(sorted_2dlist[0])):
            if sorted_2dlist[r][c] > sorted_2dlist[r+1][c]:
                return "NO"
    return "YES"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

    print(result)
    print("time :", time.time() - start)

    #     fptr.write(result + '\n')
    #
    # fptr.close()

