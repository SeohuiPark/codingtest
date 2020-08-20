

print(4 in range(0,10))


print(range(2,10)[-1])

''' 
1) 각 막대를 숫자 범위로 표현  --> 아니면 시작과 끝 숫자만. 
)) 각 막대 cnt =1 초기값 
2) 레이저 시작지점 인덱스가 그 숫자 범위안에 포함되면cnt +=1
  ** 레이저 시작 지점은 arrangement 하나씩 꺼내면서 pop(0)
  만약 그 다음 친구가 반대면 해당 인덱스 레이저 발사지점으로! 

'''
pipe1 = range(2, 18)
pipe2 = range(3, 17)
pipe3 = range(4, 10)
pipe4 = range(10, 14)
pipe5 = range(18, 22)


def solution(arrangement):
    def check_in(pipe_range, chk_num):
        if chk_num > pipe_range[0] and chk_num < pipe_range[-1]:
            return 1
        else:
            return 0

    pipe1, pipe2, pipe3, pipe4, pipe5 = range(2, 18), range(3, 17), range(4, 10), range(10, 14), range(18, 22)
    pipe1_cnt, pipe2_cnt, pipe3_cnt, pipe4_cnt, pipe5_cnt = 1, 1, 1, 1, 1
    arr = list(arrangement)
    for idx in range(0, len(arr) - 1):
        now = arr.pop(0)
        if now == "(" and arr[0] == ")":
            # print("now",idx)
            pipe1_cnt += check_in(pipe1, idx)
            pipe2_cnt += check_in(pipe2, idx)
            pipe3_cnt += check_in(pipe3, idx)
            pipe4_cnt += check_in(pipe4, idx)
            pipe5_cnt += check_in(pipe5, idx)

            # print("eachpipe",pipe1_cnt,pipe2_cnt,pipe3_cnt,pipe4_cnt,pipe5_cnt)
    return (pipe1_cnt + pipe2_cnt + pipe3_cnt + pipe4_cnt + pipe5_cnt)
