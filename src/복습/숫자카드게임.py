n, m = map(int,input().split())

card_list = [] 
for i in range(n):
    card_list.append(list(map(int,input().split())))

max_value = 0

answer = 0

for i in range(n):
    if min(card_list[i]) > max_value:
        max_value = min(card_list[i])

print(max_value)