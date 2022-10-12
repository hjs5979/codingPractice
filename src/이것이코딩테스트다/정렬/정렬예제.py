array = [7,5,9,0,3,1,6,2,4]

# 선택정렬

for i in range(len(array)):
    
    for i in range(len(array)):
        # 가장 작은 원소의 인덱스
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

print(array)

#------------------------------------------------------------------

# 삽입정렬 -> 거의 정렬되어 있을 때 빠름

for i in range(1, len(array)):
    # 인덱스 i부터 1까지 감소하며 반복하는 문법
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
        else: 
            break
print(array)

#--------------------------------------------------------------------

#퀵정렬

array = [5,7,9,0,3,1,6,2,4,8]

# def quick_sort(array, start, end):
#     if start >= end:
#         return
#     pivot = start
#     left = start + 1
#     right = end
#     while left <= right:
#         while left <= end and array[left] <= array[pivot]:
#             left += 1
#         while right > start and array[right] >= array[pivot]:
#             right -= 1
#         if left > right:
#             array[right], array[pivot] = array[pivot], array[right]
#         else:
#             array[left], array[right] = array[right], array[left]
#         quick_sort(array, start, right-1)
#         quick_sort(array, right+1, end)

# quick_sort(array, 0, len(array)-1)
# print(array)

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    
    # 피벗은 첫 번째 원소
    pivot = array[0]
    #피벗을 제외한 리스트
    tail = array[1:]
    
    #분할된 왼쪽 부분
    left_side = [x for x in tail if x <= pivot]
    #분할된 오른쪽 부분
    right_side = [x for x in tail if x > pivot]

    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

#-----------------------------------------------------------------------------------

# 계수 정렬 -> 데이터의 크기 범위가 제한되어 정수형태로 표현할 수 있을 때 사용가능, 
# 가장 큰 데이터와 작은 데이터가 1000000이상 차이가 나지 않을 때 보통 사용

# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    # 각 데이터에 해당하는 인덱스의 값 증가
    count[array[i]] += 1

# 리스트에 기록된 정렬 정보 확인
for i in range(len(count)):
    for j in range(count[i]):
        # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력
        print(i, end=' ')


