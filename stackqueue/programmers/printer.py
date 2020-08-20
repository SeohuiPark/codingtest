


'''
인쇄리스트(인덱스, 중요도 )

기준:첫값뽑아
뒤에 중요도 더 큰놈있는지 체크 max로
있으면 뒤로 보내기
없으면 기준 출력리스트에 담고(담을때 인덱스만 담기), 인쇄리스트에서 빼기

마지막에 로케 입력하면,
출력리스트에서 해당 로케값의 인덱스+1반환.
info list 가 0 될때까지

'''


# def solution(priorities, location):
#
#     print_list = []
#     info_list = [[idx, imp] for idx, imp in enumerate(priorities)]
#
#     while info_list:
#         if max([each_info[1] for each_info in info_list]) <= info_list[0][1]: # c
#             print_list.append(info_list.pop(0)[0])
#         else:
#             info_list.append(info_list.pop(0))
#     return print_list.index(location)+1
#
# t = [2, 1, 3, 2]
# print(solution(t, 2))

# print([[id, value] for id, value in enumerate(t)])






def solution(priorities, location):

    print_list = []
    info_list = [[idx, imp] for idx, imp in enumerate(priorities)]

    i = 0
    while info_list:
        print(info_list)
        if max([each_info[1] for each_info in info_list]) <= info_list[0][1]: # c
            print_list.append(info_list.pop(0)[0])

        else:
            info_list.append(info_list.pop(0))
    print(print_list)

    return print_list.index(location)+1

t = [2, 1, 3, 2]
print(solution(t, 2))

# print([[id, value] for id, value in enumerate(t)])

#
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer


#
# print(5 > i for i in t)
#
# print(any(5 > i for i in t))


def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        print(queue)
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            print(cur[1], "BACK=========> ")
            queue.append(cur)
        else:
            print(cur[1], "print")
            answer += 1
            if cur[0] == location:
                return answer

tt = [2, 1, 3,2 ]
t = [1, 1, 9, 1, 1, 1]
print(solution(tt, 0))
