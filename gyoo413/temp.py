# 백준 11651
import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: [x[1], x[0]])
for lst in arr:
    print(*lst)
# arr.sort(key=lambda x: x[1])
# start = 0
# end = 0
# new_lst = []
# while start < N: # y좌표가 같은 것들 x좌표 기준으로 정렬할거야
#     if end + 1 >= N:
#         end += 1
#         new_lst3 = arr[start:end]
#         new_lst.append(new_lst3)
#         start = end
#     else:
#         if arr[end][1]==arr[end+1][1]:
#             end +=1
#         else:
#             end += 1
#             new_lst2 = arr[start:end]
#             new_lst2.sort(key= lambda x: x[0])
#             new_lst.append(new_lst2)
#             # end+=1
#             start = end

# # print(*new_lst)
# for i in new_lst:
#     for j in range(len(i)):
#         print(*i[j])