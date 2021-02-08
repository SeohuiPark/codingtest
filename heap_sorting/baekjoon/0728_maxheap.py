import heapq
import sys

N = int(input())
heap_list = []

for idx in range(N):
    num = int(sys.stdin.readline())
    print(">>",'idx', idx,'num', num, len(heap_list))
    if num != 0:
        heapq.heappush(heap_list, (-num,num))
    else:
        try:
            print(heapq.heappop(heap_list)[1])
        except IndexError:
            print(0)

