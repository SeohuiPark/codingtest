def solution1(phone_book):
    answer = True
    hash_map = {}
    #
    # 등장한 숫자들을 count 딕셔너리로 만듦
    for phone_number in phone_book:
        hash_map[phone_number] = 1

    # 다시 숫자들을 꺼낸뒤
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:  # 숫자 하나씩 뜯어보기
            temp += number
            # 딕셔너리 키로 같은게 있지만! 전체 숫자는 다른 경우! #### 전체 숫자가 완성되기 전에 끝나도록 만들면 됨 2번 참고.
            if temp in hash_map.keys() and temp != phone_number:  ####### 근데 이렇게 할 필요 없음
                answer = False

    # print(hash_map)
    return answer


def solution2(phone_book):

    phone_book = sorted(phone_book)
    num_dict = {}
    for one_num in phone_book:
        if one_num in num_dict:
            num_dict[one_num] += 1
        else:
            num_dict[one_num] = 1

    for one_num in phone_book:
        chk = ""
        for one_digit in one_num:
            if chk in num_dict:
                return False
            else:
                chk += one_digit

    return True