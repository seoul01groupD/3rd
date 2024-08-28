# 나무 자르기

def find_height(start, end, need_tree): # 이진 탐색
    if start > end:
        return end

    mid = (start + end) // 2
    sum_tree = 0

    for tree in tree_height: # 나무 길이와의 차이 구하기
        tree_cut = tree - mid

        if tree_cut > 0: # 차이가 양수인 경우에만 추가
            sum_tree += tree_cut

    if sum_tree < need_tree: # 조건에 따라 재귀
        return find_height(start, mid-1, need_tree)

    else:
        return find_height(mid+1, end, need_tree)

N, M = map(int, input().split())
tree_height = list(map(int, input().split()))
max_height = max(tree_height)

print(find_height(0, max_height, M)) # 0과 가장 긴 나무의 길이를 각각 시작점과 끝점으로 설정