
c_list = [0,'a','b','c','d','e','f','g','h']

l = input()

r = int(l[1])

for i in range(len(c_list)):
    if l[0] == c_list[i]:
        c = i

move = [(-2,-1),(-2,-1),(-1,2),(1,2),(-2,-1),(-2,1),(1,-2),(-1,-2)]

count = 0
for m in move:
    nr = r + m[0]
    nc = r + m[1]
    if nr >= 1 & nc >= 1 & nr <= 8 & nc <= 8:
        count += 1
print(count)


