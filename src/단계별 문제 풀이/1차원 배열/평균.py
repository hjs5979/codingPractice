n = int(input())

n_list = list(map(int,input().split()))

m = n_list[0]

for i in n_list[1:]:
    if m < i:
        m = i

a = 0

for i in n_list:
    c = i/m*100
    a += c

print(a/n)