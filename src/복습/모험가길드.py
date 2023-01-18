n = int(input())
mans = list(map(int,input().split()))

mans.sort()
cnt = 0
g = 0
for i in range(n):
    g += 1
    if g >= mans[i]:
        g = 0
        cnt += 1

print(cnt)
