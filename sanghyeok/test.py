T = int(input())

for tc in range(T):
    num = int(input())
    answer = [0, 0, 0, 0, 0]
    target_nums = [2, 3, 5, 7, 11]

    for i in range(5):
        tmp_cnt = 0
        while num % target_nums[i] == 0:
            num //= target_nums[i]
            tmp_cnt += 1

        answer[i] += tmp_cnt

    print(f'#{tc + 1}', *answer)