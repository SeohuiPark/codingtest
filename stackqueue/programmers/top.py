
from collections import deque
def solution(heights):

    result = True
    result_list = deque([])
    for i in range(len(heights)-1,0,-1):
        for j in range(i-1,-2,-1):
            print(i,j)
            print(result_list)
            if heights[i] < heights[j]:
                break
            else: pass
        print(j)
        result_list.appendleft(j+1)
    result_list.appendleft(0)
    print(result_list)

h = [6,9,5,7,4]
solution(h)



from collections import deque
def solution(heights):

    result_list = deque([])
    for i in range(len(heights)-1,0,-1):
        for j in range(i-1,-2,-1):
            if heights[i] < heights[j]:
                break
            else: pass
        result_list.appendleft(j+1)
    result_list.appendleft(0)

    return list(result_list)
h = [6,9,5,7,4]
solution(h)



from collections import deque
def solution(heights):

    result_list = [0] * len(heights)
    for i in range(len(heights)-1,0,-1):
        for j in range(i-1,-1,-1):
            if heights[i] < heights[j]:
                result_list[i] = j+1
                break
    return result_list
h = [6,9,5,7,4]
solution(h)