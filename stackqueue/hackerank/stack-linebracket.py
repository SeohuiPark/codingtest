
'''
open, close value 나누기
string 에서 하나씩 뜯어서보기
1) open value list 에 속하면
open stack 에 담기

2) close value list 에 속하면
 open stack에 해당 값의 짝궁이 있는지 확인

 있다면 그짝궁 삭제해주고 cnt+=1
 짝궁이 없거나 애당초 open stack 이 없는 경우-1

3) 다 돌고 open stack 에 남는게 없으면
 cnt 출력
 남는게 있으면 -1
'''


def solution(string):


    open_value = ["(","{","[","<"]
    close_value = [")", "}", "]", ">"]
    open_stack = []
    string = list(string)
    cnt = 0
    result = True

    for token in string:
        if token in open_value:
            open_stack.append(token)

        elif token in close_value:
            close_idx = close_value.index(token)
            partner_token = open_value[close_idx]

            if len(open_stack) == 0 or partner_token not in open_stack:
                result = False
                break

            elif partner_token in open_stack:
                stack_idx = open_stack.index(partner_token)
                open_stack.remove(open_stack[stack_idx])
                cnt+=1

    if len(open_stack) ==0 and result:
        print(cnt)
    else:
        print(-1)


case1 = "Hello, World!"
case2 = "line [plus]"
case3 = "if (Counteng) {Buymilk}"
case4 = ">m<"

solution("({)}")