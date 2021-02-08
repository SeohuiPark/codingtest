import collections


def solution(participant, completion):
    '''
    1) 하나씩 돌아가며 빼기  --> runtime error

    # chk_participant = participant.copy()
    for one_com in completion:
        participant.remove(one_com)

    return participant[0]
    '''

    # 2 Counter 사용.
    part_dict = collections.Counter(participant)
    comp_dict = collections.Counter(completion)
    not_com = []
    for part_name in part_dict.keys():
        if part_dict[part_name] != comp_dict[part_name]:
            not_com.append(part_name)

    return not_com[0]