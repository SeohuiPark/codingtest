# Enter your code here. Read input from STDIN. Print output to STDOUT



'''
stack concept

매번 전체 max 를 구하기 어려우니까
max 값을 항상 끝에 두는 max stack 리스트를 만들어 둔다음에
max 물어볼때마다 끝값 반환하는 방식으로

만약? 계속 정렬을 해야하는 상황이라면 -> heap 사용.
걍 최대값만 저장해주면 되는거라면 max stack list
'''

n = int(input())

stack = []
max_stack = [] #### key point!!!!

for _ in range(n):
    info_list = list(map(int, input().rstrip().split()))
    if info_list[0] == 1:
        num = info_list[1]
        stack.append(num)
        if len(max_stack) == 0 or max_stack[-1]< num:
            max_stack.append(num)
        else:  # 가장 끝에 가장 큰 값이 유지되도록 쌓아주기
            max_stack.append(max_stack[-1])
    elif info_list[0] == 2:
        stack.pop()
        max_stack.pop() # 인덱스 맞춰서 빼주기
    else:
        print(max_stack[-1])


print("Stacklist",stack)
print("MaxStacklist",max_stack)
print("========")