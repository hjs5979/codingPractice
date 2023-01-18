from collections import Counter

n, k = map(int,input().split())

balls = list(map(int,input().split()))

c = Counter(balls)

answer = 0

sets = set(balls)

temp = len(balls)

for s in sets:
    a = c[s] * (temp - c[s])
    answer += a
    temp -= c[s]

print(answer)
    