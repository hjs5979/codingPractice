a, b, c = map(int, input().split())

n_list = [a, b, c]

m = n_list[0]

for i in n_list[1:]:
    if m < i:
        m = i

if len(set(n_list)) == 1:
    print(10000+a*1000)

if len(set(n_list)) == 2:
    if a==b:
        print(1000+a*100)
    if a==c:
        print(1000+a*100)
    if b==c:
        print(1000+b*100)

if len(set(n_list)) == 3:
    print(m*100)
