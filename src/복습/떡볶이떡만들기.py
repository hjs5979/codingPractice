n,m = map(int,input().split())

array = list(map(int,input().split()))

start = 0
end = max(array)

def cut(nums, k):
    sum_value = 0
    for num in nums:
        if num > k:
            sum_value += (num-k)

    return sum_value

while start <= end:
    mid = (start + end) // 2
    
    if cut(array, mid) == m:
        print(mid)
        break
    
    elif cut(array, mid) > m:
        start = mid + 1
    
    else:
        end = mid - 1
    