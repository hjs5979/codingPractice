n = int(input())

n_list = list(map(int,input().split()))

m = int(input())

m_list = list(map(int,input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
    
        if array[mid] == target:
            return 'yes'
        
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return 'no'

n_list.sort()

for i in m_list:
    print(binary_search(n_list,i,0,len(n_list)-1), end=' ')


# 계수정렬

# n = int(input())

# array = [0] * 1000001

# for i in input().split():
#     array[int(i)] = 1

# m = int(input())

# x = list(map(int,input.split()))

# for i in x:
#     if array[i] == 1:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')

# 집합 자료형 이용

# n = int(input())

# array = set(map(int, input().split()))

# m = int(input())

# x = list(map(int, input().split()))

# for i in x:
#     if i in array:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')
