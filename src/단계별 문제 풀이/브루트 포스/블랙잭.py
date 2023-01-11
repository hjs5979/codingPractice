from itertools import combinations
n, m = map(int, input().split())

numbers = list(map(int,input().split()))

events = combinations(numbers,3)
min_diff = 1e9
answers = []
for event in events:
    diff = m - sum(event)
    
    if diff >= 0 and min_diff > diff :
        min_diff = diff

print(m-min_diff)