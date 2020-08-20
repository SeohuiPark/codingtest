#
# def solution(prices):
#
#     ori_len = len(prices)
#     answer = [0] * ori_len
#     front_num = prices.pop(0)
#
#     for idx in range(ori_len):
#         print("-->",idx)
#         while len(prices) > 0:
#             if front_num <= prices[0]:
#                 answer[idx]+=1
#             else:
#                 answer[idx]+=1
#                 front_num = prices.pop(0)
#         front_num = prices.pop(0)
#     return answer
#
#
#
#
# def solution2(prices):
#
#     answer = [0]*len(prices)
#     stack = []
#     for i in range(len(prices)):
#         while len(stack) !=0 and prices[i] < prices[stack[len(stack)-1]]:
#             ## 만약 stack list 안에 뭐라도 있으면 (증가해온 수가 있으면)
#             ## 동시에 가장 마지막에 증가수 인덱스 값이 지금 값보다 크면     ==> 이말은 마지막 수보다 감소했다는 것임
#             # print(stack,">>",prices[i],"<",prices[stack[len(stack)-1]])
#             temp = stack.pop() #스택에서 한 수를 빼주기(마지막 증가수 인덱스빼기)
#             print("i",i,"temp",temp)
#             answer[temp] = i-temp # 마지막 현재 인덱스 - 증가수 인덱스
#         stack.append(i) ### 증가하는 수인 경우 ) 증가수 인덱스 stack list에 더해
#         print("s",stack,"a",answer)
#
#     while len(stack):
#         temp = stack.pop()
#         answer[temp] = len(prices) - temp -1
#
# aa = [1,1,1,0,0,0]
# a = [1, 2, 3, 2, 3]
# print(solution2(aa))
#
#



from collections import deque

def solution3(prices):
    answer = []
    prices = deque(prices)

    while prices: #prices 를 모두 탐색해서 [] 되면 stop

        # prices 의 첫숫자를 기준점으로 잡고
        c = prices.popleft()
        count = 0

        # 나머지 숫자 하나씩 다 살펴보기
        for i in prices:
            if c > i: # 감소하는 경우라면
                count += 1 # count+=1 하고 중단.
                break
            count += 1 # 아니면 count+=1 늘리며 계속 탐색

        answer.append(count)

        print("c",c,"\t","prices",list(prices),"\t","answer",answer)
    return answer

# aa = [1,1,1,0,0,0]
a = [1, 2, 3, 2, 3]
print(solution3(a))



def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            answer[i] += 1
            if prices[i] > prices[j]: break

    return answer



## stack FILO 으로 풀어보기

def solution(prices):
    cnt = 0
    answer = []
    min_num = prices.pop(0)
    while len(prices) >0:
        if prices[0] < min_num:
            min_num = prices.pop(0)
            answer.append(cnt)
            cnt = 0
        else:
            if cnt == len(prices)-1:
                answer.append(cnt+1)
                min_num = prices.pop(0)
                print(min_num)
                cnt = 0
            else:
                cnt +=1
                prices.pop(0)
    answer.append(0)
    # print(ans wer)
    return answer


# prices = [1,1,1,0,0,0]
a = [1, 2, 3, 2, 3]
print(solution(a))


# ## stack FILO 으로 풀어보기
#
# def solution(prices):
#     cnt = 0
#     answer = []
#     min_num = prices.pop(0)
#     while len(prices) >0:
#         if prices[0] < min_num:
#             min_num = prices.pop(0)
#             answer.append(cnt)
#             cnt = 0
#         else:
#             if cnt == len(prices)-1:
#                 answer.append(cnt+1)
#                 min_num = prices.pop(0)
#                 print(min_num)
#                 cnt = 0
#             else:
#                 cnt +=1
#                 prices.pop(0)
#
#     # print(ans wer)
#     return answer
#
# # prices = [1,2,3,0,0,0]
# a = [1, 2, 3, 2, 3]
# print(solution(a))