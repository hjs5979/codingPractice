n = int(input())

ox_list = []
for i in range(n):
    ox_list.append(input())

for ox in ox_list:
    c_list = []
    c=0
    for i in ox:
        if i == 'O':
            c+=1
        else:
            c=0
        c_list.append(c)

    a = sum(c_list)

    print(a)