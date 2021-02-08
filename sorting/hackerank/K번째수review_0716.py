



def solution(array, commands):
    result_list = []
    for info in commands:
        start, end, idx = info[0], info[1], info[2]
        slice_array = sorted(array[start-1:end])
        result_list.append(slice_array[idx-1])

    return result_list


