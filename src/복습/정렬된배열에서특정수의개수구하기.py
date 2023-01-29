from bisect import bisect_left, bisect_right

n, x = map(int,input().split())

nums = list(map(int,input().split()))

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    cnt = right_index - left_index
    
    return cnt if cnt > 0 else -1

print(count_by_range(nums,x,x))