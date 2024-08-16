import sys
import math
input = sys.stdin.readline

N,K = map(int,input().split())   # N 총인원, K 방 최대 인원

student = [[0] * 2 for _ in range(7)]   # Y는 1부터기 때문에 행은 7개로
for _ in range(N):
    S,Y = map(int,input().split())   # S 성별, Y 학년

    student[Y][S] += 1

room = 0
for i in range(7):
    for j in range(2):
        room += math.ceil(student[i][j]/K)   # 올림 함수

print(room)