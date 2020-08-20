
'''
open, close value 나누기
string 에서 하나씩 뜯어서보기


1) open value list 에 속하면 --> open stack 에 담기

2) close value list 에 속하면 open stack에 해당 값의 짝궁이 있는지 확인

 없거나 애당초 open stack 이 없는 경우 --> "NO"
 있다면 그짝궁 삭제해주고 cnt+=1
 *** 여기서 {[}] 이 허용되는 경우에는 짝궁 값을 삭제 // 안되고 오로지 [{}] 만 허용하면 pop 을 쓰는게 편함 (가장 최근애가 짝궁이어야하니까!


3) 다 돌고 open stack 에 남는게 없어야 완벽매칭  cnt 출력
   남는게 있으면 ---> "NO"
'''


##

''' 
# 1 - 범위 구해내기 
" 바로 앞뒤로 나오는 거는 레이저 구간 "
숫자 범위 구해내고, 이를 자르는 방식으로.

# 2 - 기호에 따라 의미 

2) 

( 가 나오면  open stack 에 저장 

) 의 경우는 
( 다음에 )가 나올때는 레이저 포인트 !! 
오픈스택에서 ( 하나빼주고 
그전까지 쌓여있떤 "((( " 갯수만큼 cnt 더하기 

) 다음에 ) 가 나올때는 닫힘 의미 
오픈스택에서 ( 하나빼주기 cnt+1 (꼬다리)

'''

#
# def solution(progresses, speeds):
#     stack_list = [1]
#     release_list = []
#     while len(stack_list) != 0:
#
#         print("Dd")
#
#
# solution(0, 0)

a =[1,2,3]
b = [4,5,6]

for idx, (x,y) in enumerate(zip(a,b)):
    print(idx,x,y)


print([0]*3)


t = [1]
print(sum[])