n = int(input())
for _ in range(n):
    unsorted_player_1 = list(map(int, input().split()))
    unsorted_player_2 = list(map(int, input().split()))

    m = min(unsorted_player_1[0], unsorted_player_2[0])

    player_1 = sorted(unsorted_player_1[1:], reverse=True)
    player_2 = sorted(unsorted_player_2[1:], reverse=True)

    for i in range(m):
        if player_1[i] > player_2[i]:
            print('A')
            break
        elif player_1[i] < player_2[i]:
            print('B')
            break
    else:
        if unsorted_player_1[0] == unsorted_player_2[0]:
            print('D')
        elif m == unsorted_player_1[0]:
            print('B')
        elif m == unsorted_player_2[0]:
            print('A')