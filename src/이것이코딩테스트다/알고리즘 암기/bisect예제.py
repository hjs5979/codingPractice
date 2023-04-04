# from bisect import bisect_left, bisect_right

<<<<<<< HEAD
<<<<<<< HEAD
# num_list = list(map(int, input().split()))
# target = int(input())

# # 왼쪽부터 찾음
# print(bisect_left(num_list,target))
# # 오른쪽부터 찾음
# print(bisect_right(num_list,target))

# def count_by_range(num_list, left_value, right_value):
#     right_index = bisect_right(num_list, right_value)
#     left_index = bisect_left(num_list, left_value)
#     return right_index - left_index

# print(count_by_range(num_list,4,4))


#---------------------------------------

from bisect import bisect_left, bisect_right

num_list = list(map(int, input().split()))
target = int(input())

print(bisect_left(num_list, target))
print(bisect_right(num_list, target))

def count_by_range(num_list, left_value, right_value):
    right_index = bisect_right(num_list, right_value)
    left_index = bisect_left(num_list, left_value)

    return right_index - left_index

print(count_by_range(num_list,4,4))


=======
# def count_by_range(a, left_value, right_value):
#     right_index = bisect_right(a, right_value)
#     left_index = bisect_left(a, left_value)
#     return right_index - left_index

# a = [1,2,3,3,3,3,4,4,8,9]

# print(count_by_range(a,4,4))

# print(count_by_range(a,-1,3))

from bisect import bisect_left, bisect_right

data = list(map(int,input().split()))

def count_range(data, a, b):
    l_value = bisect_left(data, a)
    r_value = bisect_right(data, b)
    
    return r_value - l_value

print(count_range(data, 3, 4))
>>>>>>> 35d42c153572b0cbd616d7fa16e0d456165c8179
=======
# def count_by_range(a, left_value, right_value):
#     right_index = bisect_right(a, right_value)
#     left_index = bisect_left(a, left_value)
#     return right_index - left_index

# a = [1,2,3,3,3,3,4,4,8,9]

# print(count_by_range(a,4,4))

# print(count_by_range(a,-1,3))

from bisect import bisect_left, bisect_right

data = list(map(int,input().split()))

def count_range(data, a, b):
    l_value = bisect_left(data, a)
    r_value = bisect_right(data, b)
    
    return r_value - l_value

print(count_range(data, 3, 4))
>>>>>>> 35d42c153572b0cbd616d7fa16e0d456165c8179
