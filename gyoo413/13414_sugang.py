import sys
input = sys.stdin.readline

k, l = map(int, input().split())
lst = [input().rstrip() for _ in range(l)]
sugang_dict = {}

for people in lst:
    if sugang_dict.get(people, False):
        sugang_dict[people] += 1
    else:
        sugang_dict[people] = 1

cnt = 0
for people in lst:
    if sugang_dict[people] == 1:
        cnt += 1
        print(people)
        if cnt == k:
            break
    else:
        sugang_dict[people] -= 1

