


# 병든 나이트



import sys
h,w = map(int,sys.stdin.readline().split())

if h ==1:
    result = 1
elif h == 2:
    print(min(4,(w+1)//2))
else:
    if w <= 6:
        print(min(4,w))
    else:
        print(w-2)

'''
높이 1 일 경우 : 1

높이 2 일 경우 :  (23 으로만 움직임) 
 가로 1,2 :1
 가로 3~ : 2
 가로 5~ : 3
 가로 7~ : 4
 그 이상은 못함 

높이 3 이상일 경우 
 가로 1,2,3,4 = 1,2,3,4
 가로 5,6,7 = 4
 가로 8~ = w-2
'''

# 30

import sys
n = list(sys.stdin.readline().rstrip())
n.sort(reverse=True)
if n[-1] != '0' or sum(map(int, n)) % 3 != 0:
    print(-1)
else:
    print(''.join(n))

#
# h,w = map(int,sys.stdin.readline().split())
# print(h,w)

