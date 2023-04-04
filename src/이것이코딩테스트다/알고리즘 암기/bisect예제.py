# from bisect import bisect_left, bisect_right

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


