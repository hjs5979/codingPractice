n = int(input())
nums = list(map(int,input().split()))
m = int(input())
targets = list(map(int,input().split()))

start = 0
end = len(nums)-1

nums.sort()

def func(start, end, nums, target):
    while start <= end:
        mid = (start + end) // 2
    
        if nums[mid] ==  target:
            return 'yes'
        
        elif nums[mid] > target:
            end = mid - 1
        
        else:
            start = mid + 1
    
    return 'no'

for target in targets:
    print(func(start, end, nums, target), end= ' ')