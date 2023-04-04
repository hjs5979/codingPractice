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
<<<<<<< HEAD
<<<<<<< HEAD
        
#---------------------------------------


n, target = map(int,input().split())

array = list(map(int,input().split()))

start = 0
end = n-1

while start <= end:
    mid = (start+end) // 2

    if array[mid] > target:
        end = mid - 1
    
    elif array[mid] < target:
        start = mid + 1
    
    else:
        print(mid)
        break
=======
            

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
        
>>>>>>> 35d42c153572b0cbd616d7fa16e0d456165c8179
=======
            

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
        
>>>>>>> 35d42c153572b0cbd616d7fa16e0d456165c8179
