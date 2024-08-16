# 수 이어가기

N = int(input())
max_num = 0
max_lst = []

for i in range(N+1):
    lst = [N, i] # 두 번째 수로 0~N의 범위 안의 한 수를 지정

    while True:
        result = lst[-2] - lst[-1] # 반복문을 통해 조건을 충족하는 리스트 생성

        if result >= 0:
            lst.append(result)

        else:
            break

    if max_num < len(lst): # 리스트의 길이가 이전 최댓값보다 길면 갱신
        max_num = len(lst)
        max_lst = map(str, lst)

print(max_num)
print(' '.join(max_lst))