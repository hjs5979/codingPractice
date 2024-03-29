def binary_search(array, start, end):
    while start <= end:
        mid = (start+end) // 2
        
        #찾은 경우 중간점 인덱스 변환
        if array[mid] == mid:
            return mid
        
        #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > mid:
            end = mid - 1
            
        #중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

n = int(input())

array = list(map(int, input().split()))

result = binary_search(array, 0, n-1)

if result == None:
    print(-1)

else:
    print(result)