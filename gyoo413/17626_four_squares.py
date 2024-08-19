# n = int(input())

# lst = [0] * (n + 1)
# sq = []
# for i in range(1, n + 1):

#     if i - int(i ** (1/2)) ** 2 == 0.0:
#         lst[i] = 1
#         sq.append(i)

#     for j in sq:
#         if i - j < 0:
#             continue
#         if (lst[i] == 0 or lst[i] > 2) and lst[i - j] == 1:
#             lst[i] = 2
#         elif (lst[i] == 0 or lst[i] > 3) and lst[i - j] == 2:
#             lst[i] = 3
#         elif lst[i] == 0 and lst[i - j] == 3:
#             lst[i] = 4


# print(lst)

n = int(input())
lst = [0] * (n + 1)
sq = []

for i in range(1, n + 1):
    
    if i - int(i ** (1/2)) ** 2 == 0:
        lst[i] = 1
        sq.append(i)

    else:
        minimum = 5
        for j in sq:
            if lst[i - j] + 1 < minimum:
                minimum = lst[i - j] + 1
        lst[i] = minimum

print(lst[-1])