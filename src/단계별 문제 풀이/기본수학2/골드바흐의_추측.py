p_list = [0 for i in range(10001)]
p_list[1] = 1
for i in range(2, 98):
    for j in range(i * 2, 10001, i):
        p_list[j] = 1
t = int(input())
for i in range(t):
    a = int(input())
    b = a // 2
    for j in range(b, 1, -1):
        if p_list[a - j] == 0 and p_list[j] == 0:
            print(j, a - j)
            break