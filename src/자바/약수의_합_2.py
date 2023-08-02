n = int(input())

n_list = list(range(1,n+1))

answer = 0

for i in n_list:
    answer += (n//i)*i

print(answer)