



def solution(numbers):
    answer = ''
    return answer



numbers = [3, 30, 34, 5, 9]
# numbers = [0,0,0,0]
print(solution(numbers))
str_list = list(map(str,numbers))
str_list.sort(key = lambda x:x*3,reverse = True)

print(str_list)


print(solution(numbers))
chk = [3, 30, 34]
print(sorted(map(str,chk))[::-1]) # 34330 > 33430,34303

'''
한자리 수랑 두자리 수랑 비교할때,
한자리수의 고유값이, 두자리수 두번째 값보다 크면, 앞으로
한자리수의 고유값이, 두자리수 두번째 값보다 작으면 뒤로!
따라서 한자리 수를 세자리 수로 늘려준다.
문자열 숫자 비교는, 자리수가 아니라 숫자 고유의 크기만을 비교한다. 

한자리수의 고유값이, 두자리수 두번째 값보다 크면, 
3을 333 으로 만들고 300을 300300300 으로 했을때 
'''


print(sorted(["333","303030"])[::-1])
print(sorted(["","300300300"])[::-1])




def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))


def solution2(numbers):
    return "".join(sorted(list(map(str, numbers)), key=lambda x: x * 3, reverse=True))


def solution3(numbers):
    str_numbers = sorted(list(map(str, numbers)), reverse=True, key = lambda x:x*3)
    return str(int(" ".join(str_numbers)))

num = [0,0,0]
print(solution(num))
print(solution3(num))




# 이 둘의 차이는