n, c = map(int,input().split())

homes = []

for _ in range(n):
    homes.append(int(input()))
    
homes.sort()

start = homes[1] - homes[0]

end = homes[-1] - homes[0]

result = 0

while start <= end:
    mid = (start + end) // 2
    
    temp = homes[0]
    cnt = 1
    for i in range(1,n):
        if homes[i] - temp >= mid:
            temp = homes[i]
            cnt += 1
    
    if cnt >= c:
        start = mid + 1
        result = mid
    else:
        end = mid -1

print(result)