# 블랙잭

N, M = map(int, input().split())
card_num = list(map(int, input().split()))
max_sum = 0

for num in card_num:
    list_for_sum = [0, 0, 0] # 선택한 카드를 넣은 리스트 준비
    list_for_sum[0] = num # 처음 자리에 숫자 하나 투입

    for other_num in card_num:

        if other_num not in list_for_sum: # 들어간 숫자와 다른 숫자 투입
            list_for_sum[1] = other_num

        else:
            continue

        for another_num in card_num:

            if another_num not in list_for_sum: # 들어간 숫자들과 다른 숫자 투입
                list_for_sum[2] = another_num
                num_sum = list_for_sum[0]+list_for_sum[1]+list_for_sum[2]

                if num_sum <= M and num_sum > max_sum: # 숫자들의 합이 조건에 맞으면 최댓값 갱신
                    max_sum = num_sum

            else:
                continue

print(max_sum)