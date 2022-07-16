n, m, k = map(int,input().split())

n_list = list(map(int,input().split()))

n_list.sort()

m1 = n_list[-1]

m2 = n_list[-2]

c1 = m//(k+1) * k + m % (k+1)
c2 = m//(k+1)

print(c1*m1 + c2*m2)
