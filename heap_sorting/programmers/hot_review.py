

import heapq


def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)

    while scoville[0]<K:
        if len(scoville)>=2:
            heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
        elif len(scoville)==1 :
            return -1
        else:
            return -1
        cnt +=1
        
    return cnt

