
#
# n = int(input())
# arr = list(map(int, input().rstrip().split()))
#
# # import collections.Counter
# def countingSort1(arr):
#     max_value = max(arr)
#     count_list = [i * 0 for i in range(100)]
#     for item in arr:
#         count_list[item] += 1
#
#     return count_list
#
# result1 = countingSort1(arr)
# print(result1)
# print(' '.join(map(str, result1)))


#----------- 다른 풀이 방법

n = int(input())
arr = list(map(int, input().rstrip().split()))

# import collections.Counter
def countingSort1(arr):
    len(arr)
    count_list = [i * 0 for i in range(len(arr))]
    for item in arr:
        count_list[item] += 1

    return count_list

result1 = countingSort1(arr)
print(result1)
print(' '.join(map(str, result1)))
