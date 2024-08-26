# 설탕 배달

N = int(input())
count = 0

while N > 0: # N이 양수인 동안
    if N % 5 == 0: # N을 5로 나눈 나머지가 0이면
        N //= 5 # N을 5로 나눠서 횟수에 추가하고 반복문 종료
        count += N
        break

    else:
        N -= 3 # 아니라면 3을 계속 빼주기
        count += 1

if N >= 0: # 반복문이 강제로 종료됐거나 N이 0이 되어서 반복문이 종료됐다면
    print(count)

else: # N이 음수가 되어서 반복문이 종료됐다면
    print(-1)