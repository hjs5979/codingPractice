from itertools import combinations

array = []

n,m = map(int,input().split())

for _ in range(n):
    array.append(list(map(int,input().split())))

chicken = []

for i in range(n):
    for j in range(n):
        if array[i][j] == 2:
            chicken.append((i,j))

events = list(combinations(chicken,m))

houses = []

for i in range(n):
    for j in range(n):
        if array[i][j] == 1:
            houses.append((i,j))
answer = 1e9
for event in events:
    distance = 0
    for house in houses:
        min_value = 1e9
        for e in event:
            d = abs(house[0]-e[0]) + abs(house[1]-e[1])
            min_value = min(min_value, d)
        distance += min_value
    
    answer = min(answer, distance)
print(answer)