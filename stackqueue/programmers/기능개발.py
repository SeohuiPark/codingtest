import math

#
def solution(progresses, speeds):
    progresses = [math.ceil((100 - a) / b) for a, b in zip(progresses, speeds)]
    answer = []
    cnt, front = 0, 0

    ## 가장 큰 수의 인덱스를 front로 저장해둠
    for idx in range(len(progresses)):
        print(idx,front)
        if progresses[idx] > progresses[front]:  # idx(들어온 수)가 front보다 크다면
            print(progresses[idx],">", progresses[front])

            answer.append(idx - front)
            print("append",idx - front)
            # front 수와 idx(들어온 수) 사이에 있던 front 보다 작은 수들 개수만큼 출시
            print("update front", front, "->", idx)
            front = idx  # update front 를idx 로 업데이트


    answer.append(len(progresses) - front)  # 맨 마지막에는 front에서 끝까지 다 출시
    print("append",len(progresses) - front)

    return answer

progresses = [93,30,55]

speeds = [1,30,5]
solution(progresses, speeds)
(progresses, speeds)

#
# def solution(progresses, speeds):
#     print(progresses)
#     print(speeds)
#     answer = []
#     time = 0
#     count = 0
#
#     while len(progresses) > 0:
#         if (progresses[0] + time * speeds[0]) >= 100:
#             progresses.pop(0)
#             speeds.pop(0)
#             count += 1
#         else:
#             if count > 0:
#                 answer.append(count)
#                 count = 0
#             time += 1
#     answer.append(count)
#     return answer
#
# '''
# 첫번째 친구가 뽑혀야 다른 친구들이 뽑히도록 pop과 time 을 이용해서 품.
# '''
#
# import math.ceil

print((100-30)/30)