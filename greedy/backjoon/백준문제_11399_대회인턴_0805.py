'''
누적합 리스트의 총합이 가장 작아지는 방향으로
'''

import sys
N = int(input())
num_list = sorted(list(map(int,sys.stdin.readline().split())))


cnt = 0
cnt_list = []
for num in num_list :
    cnt+=num
    cnt_list.append(cnt)

print(sum(cnt_list))


