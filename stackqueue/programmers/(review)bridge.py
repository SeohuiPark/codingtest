

'''
1) 다리길이 만큼 공리스트 만들기 [0,0]
2) 만약 리스트의 합이 다견무 보다 작으면 다른 하나 추가 [0,7] // (맨앞0 빼기)  // 시간 +1
3) 합이 다견무보다 크면 0을 추가 [7,0] // 맨앞 숫자빼기 // 시간 +1
4) 숫자 모두다 통과하면 끝.
'''


def solution(bridge_length, weight, truck_weights):

    bridge_list = [0]*bridge_length
    total_time = 0
    while bridge_list:
        # print(bridge_list)
        total_time+=1    # 시간하나 늘리고,
        bridge_list.pop(0)  # 맨앞에놈 뽑고,
        if truck_weights:  ### 트럭이 모두다 지나도 계속 도니까.
            if sum(bridge_list) + truck_weights[0] <=weight:
                bridge_list.append(truck_weights.pop(0)  )
            else:
                bridge_list.append(0)
    return total_time

# bridge_length, weight, truck_weights = 2,10,[7,4,5,6]
# bridge_length, weight, truck_weights = 100, 100, [10]
#
# print(solution(bridge_length, weight, truck_weights))