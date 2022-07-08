a,b = map(int, input().split())
c = int(input())

m = (b+c)%60
dh = (b+c)//60

h = (a+dh)%24

print(h, m)