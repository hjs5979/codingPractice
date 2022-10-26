#퀵정렬

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    
    tail = array[1:]
    
    left_side = [i for i in tail if i <= pivot]
    right_side = [i for i in tail if i > pivot]
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

# print(quick_sort(array))


#-----------------------------------------------------------------------------------

# 계수 정렬

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

def sort(array):
    count = [0] * (max(array)+1)
    answer = []
    
    for i in array:
        count[i] += 1
    
    for i,k in enumerate(count):
        for j in range(k):
            answer.append(i) 
    
    return answer

print(sort(array))

#-----------------------------------------------------------------------------------

# 파이썬 라이브러리 정렬

array = [5,7,9,0,3,1,6,2,4,8]

array.sort()

# print(array)

array = [('바나나',2),('사과',5),('당근',3)]

result = sorted(array, key=lambda x:x[1])
# print(result)