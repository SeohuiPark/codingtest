

open_values = ["{", "[", "("]
close_values = ["}", "]", ")"]
chk_dict = dict(zip(close_values,open_values))

user_input = list(input())
stack_list = []

for idx,key in enumerate(user_input):
    if key in chk_dict.values():
        stack_list.append(key) # 여는 기호면 stacklist 추가

    else:
        if idx ==0: # 시작부터 닫는 기호가 나온다면
            result = False # 아묻따 false
            break
        else:
            pair = stack_list.pop()
            if pair  == chk_dict[key]: # 짝궁이 맞는지 확인
                result = True
            else:
                result = False

print(result)

