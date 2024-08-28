# 병합 정렬

- 병합 정렬(Merge Sort)은 주어진 리스트를 반으로 나누고 각각의 부분 리스트를 재귀적으로 정렬한 다음, 다시 합치는 방식으로 동작하는 정렬 알고리즘
- 시간 복잡도가 항상 __O(n log n)__으로 일정함
- 다른 정렬 알고리즘과 달리 인접한 값들 간에 상호 자리 교대(swap)이 일어나지 않음

## 병합 정렬의 동작 과정
1. __분할(Divide)__ : 리스트를 절반으로 나누어, 리스트의 크기가 1이 될 때까지 계속해서 나눔
2. __정복(Conquer)__ : 각 부분 리스트를 정렬
3. __병합(Merge)__ : 나뉜 리스트를 병합하면서 정렬된 하나의 리스트로 만듬. 
__병합 할 때는 두 리스트의 첫 번째 원소부터 비교하면서 작은 값을 순서대로 새로운 리스트에 넣기__
```
def merge_sort(arr):
    # 리스트의 크기가 1 이하일 경우 그대로 반환 (base case)
    if len(arr) <= 1:
        return arr

    # 리스트를 반으로 나눔
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # 재귀적으로 나뉜 부분 리스트들을 정렬
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # 두 개의 정렬된 리스트를 병합
    return merge(left_sorted, right_sorted)

def merge(left, right):
    sorted_list = []
    left_index, right_index = 0, 0

    # 두 리스트를 비교하며 작은 값을 새로운 리스트에 추가
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    # 남은 요소가 있을 경우 모두 추가
    sorted_list.extend(left[left_index:])
    sorted_list.extend(right[right_index:])

    return sorted_list
```

## 예시
```
[6,5,3,1,8,7,2,4]

[6,5,3,1] [8,7,2,4]

[6,5] [3,1] [8,7] [2,4]

[6] [5] [3] [1] [8] [7] [2] [4]

[5,6] [1,3] [7,8] [2,4]

[1,3,5,6] [2,4,7,8]

[1,2,3,4,5,6,7,8]
```

## 병합 정렬의 시간 복잡도
- __분할 단계__ : 리스트를 계속해서 반으로 나누므로 O(log n)
- __병합 단계__ : 병합 단계에서 각 단계마다 전체 리스트를 한 번씩 순회 O(n)
- 전체 시간 복잡도는 O(n log n)

## 병합 정렬의 장점과 단점
- 장점:
   - 시간 복잡도가 항상 O(nlog n)으로 일정하므로, 최악의 경우에도 효율적
   - 대용량 데이터 다룰 때 효과적
   - 안정적인 정렬 방법

- 단점:
  - 추가적인 메모리 공간이 필요
  - 작은 데이터 집합에서는 다른 정렬 알고리즘보다 효율이 떨어질 수 있음
