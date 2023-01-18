numbers = list(map(int,input().split()))

numbers.sort()

target = 1
for n in numbers:
    if target < n:
        break
    else:
        target += n

print(target)
        