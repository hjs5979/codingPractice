n = int(input())

l = list(map(int, input().split()))

l.sort()

print(l)

target = 1
for x in l:
    if target < x:
        break
    target += x

print(target)