
# 최대힙에서 응용
import heapq
import sys

N = int(input())
heap_list = []

for idx in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap_list, (abs(num),num))
    else:
        try:
            print(heapq.heappop(heap_list)[1])
        except IndexError:
            print(0)
