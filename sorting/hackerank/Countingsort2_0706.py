
#### for hackerank ver


n = int(input())
arr = list(map(int, input().rstrip().split()))


def countingSort2(arr):
    count_list = [i*0 for i in range(100)]
    for item in arr:
        count_list[item]+=1
    sorted_list = []

    for count, num in zip(count_list, range(100)):
        if count == 0 :
            pass
        else:
            num_list = [num for i in range(count)]
            sorted_list.extend(num_list)
    return sorted_list

result2 = countingSort2(arr)
print(result2)
print(' '.join(map(str, result2)))


# Basic count sorting


n = int(input())
arr = list(map(int, input().rstrip().split()))


def countingSort2(arr):
    count_list = [i*0 for i in range(len(arr))]
    for item in arr:
        count_list[item]+=1
    sorted_list = []

    for count, num in zip(count_list, range(len(arr))):
        if count == 0 :
            pass
        else:
            num_list = [num for i in range(count)]
            sorted_list.extend(num_list)
    return sorted_list

result2 = countingSort2(arr)
print(result2)
print(' '.join(map(str, result2)))


#----------- 다른 풀이 방법
## https://ratsgo.github.io/data%20structure&algorithm/2017/10/16/countingsort/

n = int(input())
arr = list(map(int, input().rstrip().split()))


A=[2,0,2,0,4,1,5,5,2,0,2,4,0,4,0,3]
[5,6,10,11,14,16]

def countingSort_new(arr):

    # define count list
    count_list = [0] * len(arr)
    for item in arr:
        count_list[item]+=1


    # add count_list
    a_count_list = count_list.copy()
    for i in range(len(a_count_list)-1):
        a_count_list[i+1] += a_count_list[i]


    # define output array
    output_list = [-1] * len(arr)

    # fill output array
    ''' 뒤에서부터 요소를 꺼내고, 해당 요소의 누적카운트에 위치에 넣고 / -1 하기 --> 다음에 자리  '''
    for num in reversed(arr):
        input_idx = a_count_list[num]-1
        output_list[input_idx] = num
        a_count_list[num] -=1

    print(count_list)
    print(a_count_list)
    print(output_list)

countingSort_new(arr)


'''
입력 
5
1 1 3 2 1
count array 는 [0, 3, 1, 1, 0] ==> 누적 리스트로 변경 [0,3,4,5,0] 

누적 리스트는 아웃풋 리스트에 들어갈 숫자의 인덱스가 됨 
1번째~3번째 :1 / 4번째 :2 / 5번째 :3

따라서 
1)  array의 뒤에서 부터 하나씩 꺼냄 
"1" 의 경우 count에서 3임 ==> 아웃풋 리스트에 1,2,3 번째에 들어감  

2) 얘를 3번에 넣고, count -1 로 빼줌 (다음 "1" 이 두번째에 들어가도록) 

이 과정 반복. 

'''
''' 입력된 숫자에 해당하는 카운트누적리스트의 값이 해당 숫자의 마지막 인덱스에 해당함 
  탐색숫자 4 --> 카운트누적리스트에서 4번째 값이 5이고, 5번째값 7이면--> 즉 ?,?,?,5,7
  실제 정렬리스트에서 
      6,7번째에서 마지막 4가 등장한다는 것 / 5번째까지 3이 등장한다는 것 ==> ?,?,?,?,3,4,4
  따라서 생성한 정렬리스트 7번째에 4 넣어주고, 카운트누적리스트의 값빼주면, 4가 2번째로 나올때 6번째에 들어감  '''





