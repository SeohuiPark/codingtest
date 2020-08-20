
import heapq


import heapq
from collections import deque
def solution(stock, dates, supplies, k):
    cnt = 0
    h = []
    dates = deque(dates)
    supplies = deque(supplies)
    for now in range(1, k):
        stock-=1
        if len(dates) == 0 or stock > k:
            break
        else:
            if now == dates[0]:
                heapq.heappush(h, (-supplies[0], supplies[0]))
                dates.popleft()
                supplies.popleft()
                if stock >= now:
                    pass
                else:
                    stock += heapq.heappop(h)[1]
                    cnt += 1
            else:
                pass
    return cnt

dates  = [4,10,15]
supplies = [20,5,10]
k = 30
stock = 4
a = solution(stock, dates, supplies, k)
print("A",a)
