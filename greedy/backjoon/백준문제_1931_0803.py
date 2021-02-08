
'''
시작 숫자 기준으로 하나씨 ㄱ리스트 만들어

((0, 6, 6), (6, 10, 4) (12, 14, 2)]
(1, 4, 3), (5, 7, 2), (8, 11, 3),  (12, 14, 2)]
(2, 13, 11), 
(3, 5, 2), (5, 7, 2)or (6, 10, 4)   (12, 14, 2)]
(3, 8, 5), (8, 11, 3) (12, 14, 2)]


만약 끝수랑 같거나 큰게 나오면 거기에 쌓아줘 
근데 같은 시작시점인데 숫자가 더 길면 버려? 

 (5, 9, 4), 
'''

### 가장 먼저 끝나는 걸 찾는다는 컨셉으로 다시 풀기

import sys

N = int(input())
info_list = []
for idx in range(N):
    sta, end = map(int, sys.stdin.readline().split())
    info_list.append((sta,end))
info_list = sorted(info_list, key = lambda x: (x[1], x[0]))

end_point = info_list[0][1]
chk = 1

for info in info_list[1:]:
    st, en = info[0], info[1]
    if (st >=  end_point):
        print(info)
        end_point = en
        chk+=1

print(chk)

#
# # 1931.py
# def compare(elem):
#     #elem1 은 end, elem0 은 start
#     return (elem[1], elem[0])
# reps=int(input())
# total=[]
# for t in range(reps):
#     start, end=input().split(" ")
#     total.append((int(start), int(end)))
# total.sort(key=compare)
#
# _end=total[0][1]
# found=1
# for i in range(1, len(total)):
#     if(total[i][0]>=_end):
#         _end=total[i][1]
#         found+=1
# print(found)
#
# print(total)
# print("mmmm")

