# 색종이

paper = int(input())
borad = [[False] * 101 for _ in range(101)] # 101 * 101 크기의 False 2차원 배열
paper_loca = []
count = 0

for _ in range(paper):
    x, y = map(int, input().split())
    paper_loca.append((x, y)) # 주어진 좌표를 튜플로 리스트에 저장

for loca in paper_loca:
    for i in range(loca[0], loca[0] + 10):
        for j in range(loca[1], loca[1] + 10): # 좌표로부터 위 아래 10씩 안의 범위에서
            if borad[i][j] == False: # False면 True로 바꾸고 횟수(넓이) +1
                borad[i][j] = True
                count += 1

print(count)