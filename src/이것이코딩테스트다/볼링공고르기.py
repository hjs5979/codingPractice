n, m = map(int, input().split())

l = list(map(int, input().split()))

array = [0] * 11

for i in l:
    array[i] += 1

answer = 0

for j in range(1, m+1):
    n -= array[j]
    answer += array[j]*n

print(answer)
    