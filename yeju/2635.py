import sys
input = sys.stdin.readline

N = int(input())
cnt = 1   # 초기 횟수
arr = [N]   # 처음값 넣어주기

# 재귀를 이용하여 계속해서 빼기를 실행하는 함수
def decrease(N,i):
    global cnt
    if i < 0:   # 음수가 되면 출력
        return cnt,arr   # 연산횟수, 연산과정
    else:
        cnt += 1   # 함수가 한 번 시행될 때마다 +1
        arr.append(i)   # 과정을 나타내기 위한 리스트
        i = N-i   # f[N+2] = F[N] - F[N+1]
        return decrease(N - i,i)   # 다시 해당 함수를 통해 값 계산

all = []
# 1부터 N까지 숫자를 대입하며, 가장 연산횟수가 많은 값과 그 과정을 추출
for i in range(1,N+1):
    result = decrease(N,i)
    all.append(result)
    cnt = 1
    arr = [N]

all.sort(reverse=True)   # 내림차순 정렬로 가장 큰 값이 맨 앞에 오게끔

print(all[0][0])
print(*all[0][1])