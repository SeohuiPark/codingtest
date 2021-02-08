#
# from collections import deque
#
# def solution(bridge_length, weight, truck_weights):
#
#     # 1. init
#     wait_list = deque(truck_weights)
#     bon_list = deque([])
#     bon_truck_sum = 0
#     f_list = deque([])
#     total_time = 1
#
#     # 2. loop
#     while len(f_list) != len(truck_weights):
#         if len(wait_list)>0:
#             next_truck = wait_list[0]
#             if bon_truck_sum + next_truck <= weight:
#                 now_truck = wait_list.popleft()
#                 bon_list.append([now_truck,bridge_length])
#
#         total_time+=1 # 전체 시간 1증가
#         # bon_list 리스트에 있는 트럭시간 -1 /  트럭시간 다된친구 삭제 /
#         up_bon_list = []
#         for t in bon_list:
#             if t[1] > 1:
#                 up_bon_list.append([t[0], t[1] - 1])
#                 bon_truck_sum += t[0]
#             else:
#                 f_list.append(t[0])
#                 bon_truck_sum -= t[0]
#         bon_list = up_bon_list.copy()
#
#         print("total_time",total_time)
#         print("wait_list",wait_list)
#         print("bon_list", bon_list)
#         print("f_list", f_list)
#         print("bon_truck_sum",bon_truck_sum)
#
#
#     return total_time
#
#
# bridge_length = 100
# weight = 100
# truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
# # weight_list = deque(truck_weights)
# # print(weight_list[0])
# print(solution(bridge_length, weight, truck_weights))
# #
# #
# #
# # # num_list = [1,2,3,4,5]
# # # d_num_list = deque(num_list)
# # # d_num_list.popleft()
# # # print(d_num_list)
# # #
# # #
# # # bridge_list = []
# # # time = 2
# # # truck_weight = 7
# # # bridge_list.append([truck_weight])
# # # print(bridge_list)
# # # truck_time_dict = dict(zip(range(len(d_num_list)), [2] * len(d_num_list)))
# # # print(truck_time_dict)
# # #
# bon_truck_sum = 0
# bon_list = [[7,2],[4,1],[5,2]]
# new = []
# f_list = []
#
# up_bon_list = []
# for t in bon_list:
#     print("1",t)
#     if t[1]>1:
#         up_bon_list.append([t[0],t[1]-1])
#         bon_truck_sum+=t[0]
#     else:
#         print("REMOVE",t)
#         f_list.append(t[0])
#         bon_truck_sum -= t[0]
#
# print(bon_list)
# print(up_bon_list)
# print(f_list)
# print(bon_truck_sum)
#
# #
# # # update = list(filter(lambda x: [x[0],x[1]-1] not x[1]<=1 ,num_list_2d))
# # # print(update)
# # # update = list(map(lambda x: [x[0],x[1]-1] if x[1]>1 else None,num_list_2d))
# # # update = [[x[0],x[-1]-1] if x[1]>1 else new.append(x) for x in num_list_2d ]
# # # print(update)
# # # print(new)
#
# t = deque([7,4,5,6])
#
# a = t.popleft()
# print(t)


def solution(bridge_length, weight, truck_weights):
    total_time = 0
    bridge = [0] * bridge_length

    while bridge:
        total_time += 1
        print("Time",total_time, "Bridge",bridge)
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
            print(">> update",bridge)
    return total_time

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
# print(">>>",truck_weights.pop())
# weight_list = deque(truck_weights)
# print(weight_list[0])
print(">>",solution(bridge_length, weight, truck_weights))


