r, c = map(int,input().split())
answer = 0
for i in range(r):
    n_list = list(map(int,input().split()))
    min_value = min(n_list)
    answer = max(answer,min_value)

print(answer)    