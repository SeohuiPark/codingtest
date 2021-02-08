import sys



'''
team_av = girl+boy-intern 이거 일단 
3으로 나눠보기  ==> team_num 2임


만약 girl 숫자 2*2넘고, boy 숫자 1*2 넘으면 --> 해당 값이 팀갯수 
아니면 team_num1



'''


girl,boy,intern = map(int,sys.stdin.readline().split())

team_av = (girl+boy-intern)//3
while team_av > 0:
    if girl > 2*team_av and boy > team_av:
        break
    else:
        team_av-=1
print(team_av)



### 런타임에러
'''
7명이서 만든다고 하면
2명 *2/ 1명 *2 :6명 ㄱㅊ
2명 *3 / 1명*3 :9 오바
팀이 아무리 늘어봤자. 여자/2한 값보다 크지는 못함. 
# '''
girl,boy,intern = map(int,sys.stdin.readline().split())

team_av = girl+boy-intern

for t in range(1,(girl//2)+1):
    if (2*t + 1*t) < team_av:
        pass
    elif (2*t + 1*t) == team_av:
        print(t)
        break
    else:
        print(t-1)
        break






# ## 런타임 에러
# girl,boy,intern = map(int,sys.stdin.readline().split())
#
# team = 0
# while True:
#     if girl>1 and boy>0:
#         girl -=2
#         boy -=1
#         team +=1
#         if (girl + boy) > intern:
#             pass
#         elif (girl + boy) == intern:
#             break
#         else:
#             team-=1
#             break
#     else:
#         break
#
# print(team)