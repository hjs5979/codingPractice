n = int(input())

nums = list(map(int,input().split()))

answer = -1

start = 0
end = len(nums) - 1

while start <= end:
    # print(start, end)
    
    mid = (start + end) // 2
    
    if mid == nums[mid]:
        answer = mid
        break
    elif mid > nums[mid]:
        start = mid + 1
    else:
        end = mid - 1

print(answer)