# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid
        
#         elif array[mid] > target:
#             end = mid - 1
        
#         else:
#             start = mid + 1
    
#     return None

# n,target = list(map(int, input().split()))

# array = list(map(int, input().split()))

# result = binary_search(array, target, 0, n-1)

# if result == None:
#     print('없음')

# else:
#     print(result+1)
            

# ------------------------------------------

n,target = map(int, input().split())

data = list(map(int,input().split()))

start = 0
end = len(data) - 1

while start <= end:
    mid = (start+end) // 2
    
    if data[mid] == target:
        print(mid)
        break
    
    if data[mid] > target:
        end = mid - 1
        
    else:
        start = mid + 1
        