n, m, k = map(int, input().split())

n_list=list(map(int,input().split()))
n_list.sort(reverse=True)

answer = 0

a = m//k
b = m%k

answer = (k * n_list[0])* a + n_list[1] * b

print(answer)