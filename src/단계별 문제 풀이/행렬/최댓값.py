array = []

for i in range(9):
    array.append(list(map(int,input().split())))

value = 0
r = 0
c = 0
for i in range(9):
    for j in range(9):
        if array[i][j] > value:
            value = array[i][j]
            r = i+1
            c = j+1

print(value)
print(r, c)