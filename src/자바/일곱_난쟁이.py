from itertools import combinations

height_list = []

for i in range(9):
    height_list.append(int(input()))

for i in list(combinations(height_list,7)):
    if sum(i)==100:
        answer = list(i) 
        break

answer.sort()
for j in answer:
    print(j)