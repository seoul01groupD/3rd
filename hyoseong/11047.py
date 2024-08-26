# 동전 0

N, K = map(int, input().split())
price_lst = [int(input()) for _ in range(N)]
coin = 0 # 사용한 동전 개수 초기화

for price in reversed(price_lst): # 높은 가격부터
    coin += K//price # 목표 값을 가격으로 나눈 몫을 개수에 추가
    K %= price # 목표 값은 나머지로 변경

print(coin)